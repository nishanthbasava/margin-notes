## Terms that I have had to look up on this topic

# Auxillary Information
Auxillary information refers to external context provided at inference time, such as prompt instructions, task descriptions, semantic attributes, or few-shot examples, that guides the model on how to perform a task without altering its parameter.

In contrast, post-training (which includes fine-tuning, RLHF, or domain-specific adaptation) involves updating the model's weights using additional datasets after the initial pre-training phase. 

# Zero-shot Generalization
You do not need to post-train or fine-tune an already pre-trained model on specific labeled data for a new task. The pre-training phase, where the model learns broad representations, logic, and concepts from massive datasets, is entirely required.

Zero-shot capabilities rely directly on taht pre-trained foundation to interpret the auxiliary information provided in the prompt and complete the task on the fly.


# Few-shot Learning (FSL) 
N-shot learning: a subset of ML that also includes FSL and one-shot learning. 
Few-shot learning typically uses transfer learning and meta learning-based methods to train models ot quicklky recognize new classes with only a few labaeled training examples-or, in one-shot learning, a single labeled example.


# Self-supervised Learning (SSL)
