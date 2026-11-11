## Basically just writing any doubts I have about transformers and random questions here

# What does the MLP layer do and how does it work?
1. Higher Capacity for Feature Combination
2. Non-Linear Transformations
3. Acting as a Key-Value Memory

3B1B explanation:
- MLP layer has about 2/3 of the model parameters, they allow extra capacity for the model to store facts.
- Linear, ReLU, then another Linear

rewatch the DL Chapter 5 and 6 videos for KV caching 


# What is Batch Training
- Updating model weights using the averaged loss over a group of examples at once, instead of one example at a time.
- Stack N examples into one tensor (batch_size, seq_len), run one forward pass, compute the mean loss, one backward pass, one optimizer step
- WHY?: GPUs parallelize across the batch (much faster), and averaging gradients over many examples gives a less noisy, more stable gradient estimate
- mini batches are like 32-512 examples
- Trade off: bigger batches -> smoother gradients + better hardward utilization, but mroe memory and sometimes worse generalization


# KV-Caching


# Layer Normalization
Layer Normalization is placed right before or after the attention and MLP blocks (often called pre-LN or post-LN). Its main job is to stabilize the numbers flowing through the network so training doesn't blow up or vanish. 

For each individaul token's vector in the residual stream, LayerNorm looks across its dmodel dimensions and calculates their mean and variance and normalizes them so that 
- Values have a mean of 0 (centered) and a variance of 1 (standardized scale)

Applies Learned Scaling and Shiftring (gamma and beta)
- gamma is for scaling: multiplies the normalized values to stretch or shrink the variance back to whatever magnitude is optimal for the network.
- beta for shifting: Adds an offset to move the mean wherever the model needs it.

Look into how these parameters are learned during training.

Why is LN important?
- Prevents activation explosion: As numbers pass through dozens of attention and MLP layers, they can rapidly grow in magnitude (or shrink to zero). LayerNorm keeps the scale of the vectors under control.
- Smooths Training. It ensures that no single dimension dominates the vector just because it has larger numbers, making gradient descent much more stable and efficient. 


Attention is all about communication between tokens. It looks across the sequence and lets words pass informatino to each other (making sure the token for "Jordan" knows about "Michael")
MKLPs (Multi-Layer Perceptrons) are all about processing and recall. Because they take each token's vector and run it throug the massively expanded hiddne space (4*d_model), they act like a massive knowledge bank or pattern matcher. 


# Maximum Likelihood Estimation (MLE) in NLP

