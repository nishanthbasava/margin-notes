#hugging face abstraction

import torch
from datasets import load_dataset
from peft import LoraConfig
from transformers import AutoTokenizer
from trl import SFTConfig, SFTTrainer
from trl.chat_template_utils import get_training_chat_template

dataset = load_dataset("trl-lib/Capybara", split="train").shuffle(seed=0).select(range(4000))

# The Base model's tokenizer has no training-compatible chat template, and letting
# trl clone one (chat_template_path) adds dummy tokens that trip a peft bug
# (TrainableTokensWrapper). Instead: borrow the instruct model's template,
# pre-patched with {% generation %} markers for assistant-only loss.
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen3-1.7B-Base")
tokenizer.chat_template = get_training_chat_template(AutoTokenizer.from_pretrained("Qwen/Qwen3-1.7B"))
tokenizer.eos_token = "<|im_end|>"  # ChatML turn terminator, so generation stops after the reply

trainer = SFTTrainer (
    model="Qwen/Qwen3-1.7B-Base",
    processing_class=tokenizer,
    train_dataset=dataset,
    peft_config=LoraConfig(r=16, lora_alpha=32, lora_dropout=0.05, 
                           target_modules="all-linear", task_type="CAUSAL_LM"),
    args=SFTConfig(output_dir="qwen3-sft-lora-trl",
                   model_init_kwargs={"dtype": torch.bfloat16},
                   max_length=1024,
                   per_device_train_batch_size=4,
                   gradient_accumulation_steps=4,
                   learning_rate=2e-4,
                   lr_scheduler_type="cosine",
                   warmup_steps=10,
                   num_train_epochs=1,
                   bf16=True,
                   gradient_checkpointing=True,
                   assistant_only_loss=True, #same masking as the manual script, es
                   # essentially we only want the model to be training on ITS outputs, not on predicting the user prompts.
                   logging_steps=10,
                   report_to="none"
                   #set to "wandb" once you want curves)
        ),
)

trainer.train()
trainer.save_model()

## SCHEMA FOR DATASETS (for when I import other Hugging Face datasets)
#num_rows = 4000, I'm selecting 4000 examples
#

print(dataset[0])            # full first example
print(dataset[0]["messages"])

#

#TRL stands for Transformer RL, but now it's a general post-training toolkit. 
#SFTTrainer is its most useful piece but its just plain SFT with no RL
#when you clone you must run python -m venv .venv && pip install -r requirements.txt to rebuild the virtual environment


# Potentially test on GLUE benchmark? maybe there are others

#"Inductive Biases" are assumptiosn that other neural network architectures assume about data when making predictions

# RNNs are weak at long-range dependencies and can't parallelize across the sequence
# like the hidden state is passed from each input so like if X1 impacts X100 its hidden state is lost during the recurrence
# Attention lets every token look at every other token directly, with weights computed from the content itself. 
# Parallelizable, handles long range well. And is what ALL LLMs use.
            # What if could invent a new LLM architetype without use of attention mechanisms?

# GNNs for graphs like molecules or social networks. Nodes update by aggregating messages from their neighbors.
# State-space models (Mamba): a newer sequence architecture, RNN-like recurrence but parallizable in training, linear cost in sequence length versus attention's quadratic
