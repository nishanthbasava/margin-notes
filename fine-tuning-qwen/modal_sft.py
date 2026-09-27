import subprocess
from pathlib import Path
import modal

HERE = Path(__file__).parent
app = modal.App("qwen3-sft")

image = (modal.Image.debian_slim(python_version="3.11")
         .pip_install("torch", "transformers", "peft", "trl", "datasets", "accelerate")
         .add_local_file(HERE / "sft_trl.py", "/root/sft_trl.py"))

hf_cache = modal.Volume.from_name("hf-cache", create_if_missing=True)
out = modal.Volume.from_name("sft-out", create_if_missing=True)

@app.function(image=image, gpu="A10G", timeout=2 * 60 * 60,
              secrets=[modal.Secret.from_name("huggingface")],
              volumes={"/root/.cache/huggingface": hf_cache, "/out": out})
def train():
    subprocess.run(["python", "/root/sft_trl.py"], cwd="/out", check=True)