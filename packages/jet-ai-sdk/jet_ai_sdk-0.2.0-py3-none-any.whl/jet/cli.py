import argparse, os, json
from pathlib import Path
import mlflow
from mlflow import MlflowClient
from datasets import load_dataset
from jet.train import train_with_options
from jet.eval import Evaluator
from jet.merge import merge_lora

def _bool(s): return str(s).lower() in {"1","true","yes","y","on"}

def train_cmd(args):
    with mlflow.start_run():
        mlflow.log_params(vars(args))
        if os.path.isdir(args.dataset_id):
            print("📁 Loading local dataset...")
            # For local datasets, we'll try to load them as a directory
            # This is a basic implementation - in production you'd want more robust handling
            try:
                from datasets import Dataset
                import json
                
                # Try to load as JSONL first
                jsonl_files = list(Path(args.dataset_id).glob("*.jsonl"))
                if jsonl_files:
                    data = []
                    for file in jsonl_files:
                        with open(file, 'r', encoding='utf-8') as f:
                            for line in f:
                                data.append(json.loads(line.strip()))
                    ds = Dataset.from_list(data)
                else:
                    # Fallback to loading as directory
                    ds = load_dataset(args.dataset_id, split=args.split, streaming=False)
            except Exception as e:
                raise SystemExit(f"Failed to load local dataset '{args.dataset_id}': {e}")
        else:
            ds = load_dataset(args.dataset_id, split=args.split, streaming=False)
        text_field = args.text_field or "text"
        class Opts:
            model=args.model; output_dir=args.output_dir
            per_device_batch=args.per_device_batch; grad_accum=args.grad_accum
            lr=args.lr; epochs=args.epochs; seed=42; engine=args.engine
            text_field=text_field; max_seq=args.max_seq
            merge_weights=args.merge_weights
            do_sample=args.do_sample; temperature=args.temperature
            top_p=args.top_p; top_k=args.top_k
        job = train_with_options(Opts, train_ds=ds, eval_ds=None)
        mlflow.log_artifacts(job.model_dir, artifact_path="model_dir")
        if getattr(job, "merged_dir", None):
            mlflow.log_artifacts(job.merged_dir, artifact_path="merged_dir")
        run = mlflow.active_run()
        if run:
            mv = mlflow.register_model(f"runs:/{run.info.run_id}/model_dir", name="jet-mvp")
            client = MlflowClient()
            client.set_model_version_tag("jet-mvp", mv.version, "base_model", args.model)

def evaluate_cmd(args):
    with mlflow.start_run():
        mlflow.log_params({"eval_model": args.model_dir_or_id})
        ev = Evaluator(args.model_dir_or_id, do_sample=True, max_new_tokens=32)
        out = ev.evaluate(["Hello"], references=None, perplexity_texts=["Hello world."])
        mlflow.log_dict(out, "eval.json")
        print(json.dumps(out, indent=2))

def package_cmd(args):
    out_dir = merge_lora(args.base_model, args.adapter_dir, args.out_dir)
    print(json.dumps({"merged_dir": out_dir}))
    if mlflow.active_run():
        mlflow.log_artifacts(out_dir, artifact_path="merged_dir")

def api_cmd(args):
    """Start the Jet AI API server"""
    try:
        from .api.cli import main as api_main
        # Override sys.argv to pass arguments to the API CLI
        import sys
        original_argv = sys.argv
        sys.argv = ["jet-api"] + (args.api_args or [])
        try:
            api_main()
        finally:
            sys.argv = original_argv
    except ImportError:
        print("❌ API dependencies not installed. Install with: pip install jet-ai-sdk[api]")
        sys.exit(1)

def main():
    p = argparse.ArgumentParser(description="Jet AI CLI")
    sub = p.add_subparsers(dest="cmd", required=True)
    
    # Training command
    tp = sub.add_parser("train")
    tp.add_argument("--model", required=True)
    tp.add_argument("--dataset_id", required=True)
    tp.add_argument("--split", default="train")
    tp.add_argument("--text_field", default="text")
    tp.add_argument("--engine", default="auto")
    tp.add_argument("--output_dir", default="/workspace/outputs/run")
    tp.add_argument("--epochs", type=int, default=1)
    tp.add_argument("--per_device_batch", type=int, default=1)
    tp.add_argument("--grad_accum", type=int, default=8)
    tp.add_argument("--lr", type=float, default=2e-4)
    tp.add_argument("--max_seq", type=int, default=2048)
    tp.add_argument("--merge_weights", type=_bool, default=False)
    tp.add_argument("--do_sample", type=_bool, default=True)
    tp.add_argument("--temperature", type=float, default=0.7)
    tp.add_argument("--top_p", type=float, default=0.9)
    tp.add_argument("--top_k", type=int, default=50)
    tp.set_defaults(func=train_cmd)
    
    # Evaluation command
    ep = sub.add_parser("evaluate")
    ep.add_argument("--model_dir_or_id", required=True)
    ep.set_defaults(func=evaluate_cmd)
    
    # Package command
    pp = sub.add_parser("package")
    pp.add_argument("--base_model", required=True)
    pp.add_argument("--adapter_dir", required=True)
    pp.add_argument("--out_dir", required=True)
    pp.set_defaults(func=package_cmd)
    
    # API server command
    ap = sub.add_parser("api")
    ap.add_argument("api_args", nargs="*", help="Arguments to pass to the API server")
    ap.set_defaults(func=api_cmd)
    
    args = p.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
