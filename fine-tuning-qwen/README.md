## sft_trl.py
A complete, runnable training script. LoRA fine-tuning of Qwen3-1.7B-Base on 4,000 examples of the Caybara chat dataset using TRL's SFTTrainer. 
- 1.7 Billion learned weights.
- "Base" means that a model has only been pretrained.
- It learned to predict the next token over a huge pile of internet text, but hasn't gone through the post-training that turns a model into an assistant.
- Alibaba also released Qwen3-1.7B, which is post-trained, chat-ready version


## Capybara
- Multi-turn conversation dataset. 
- Generated using Amplify-Instruct, which is where you start with a seed question and ask a teacher model to generate "amplified" prompts with more layers of complexity.

Essentially, I took a raw pretrained model that can only continue text and instruction-tuned it into a multi-turn chat assistant, using LoRA on 4,000 example conversations.

SFT at this scale mostly teaches behavior and format, not new knowledge. The model already "knows" things from pretraining. 