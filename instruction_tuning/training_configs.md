# Model
model_name: Qwen/Qwen2.5-0.5B-Instruct
max_seq_length: 512

# Dataset
train_file: data/train.jsonl
eval_file: data/validation.jsonl

# Training
epochs: 3
learning_rate: 0.0002
batch_size: 4
gradient_accumulation_steps: 4
optimizer: adamw
seed: 42

# LoRA
lora_rank: 8
lora_alpha: 16
lora_dropout: 0.05
target_modules:
  - q_proj
  - v_proj

# Evaluation and logging
eval_steps: 100
logging_steps: 10
save_steps: 100

# Output
output_dir: outputs/qwen-fmri-qc