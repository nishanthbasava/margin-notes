# Instruction Tuning for Large Language Models: A Survey
## Zhang et al. 2025
https://arxiv.org/abs/2308.10792

Instruction Tuning (IT) = Supervised Fine-Tuning (SFT)

Involves further training LLMs using (Instruction, output) pairs
- Instruction: human instructions for the model
- Output: desired output that follows the given instructions

Primary Benefits:
- Finetuning an LLM on the insutrction dataset bridges the gap between the NEXT-WORD PREDICTION objective of LLMs and the users' objective of instruction following

- SFT allows for a more controllable and predictable model behavior compared to standard LLMs

- SFT is computationally efficient and can help LLMs rapidly adapt to a specific domain without extensive retraining or architectural changes. 


Opportunities for improvement
- Improving instruction adherence
- Handling unanticipated model responses

Analysis/Discussion Topics of interest:
- Pre-training methods
- Reasoning abilities
- Downstream applications


Pre-training:


Training process:
- Loss masking; run 
- Training: standard teacher-forced autoregressive training: at each response position, 


What is autoregressive training and what is meant by "teacher-forced"?

What is 


LoRA