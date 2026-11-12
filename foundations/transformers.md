## Basically just writing any doubts I have about transformers and random questions here

# What does the MLP layer do and how does it work?
1. Higher Capacity for Feature Combination
2. Non-Linear Transformations
3. Acting as a Key-Value Memory

3B1B explanation:
- MLP layer has about 2/3 of the model parameters, they allow extra capacity for the model to store facts.
- Linear, ReLU, then another Linear

Attention moves information between tokens; the MLP does nonlinear computation on each token independently. Superposition is a property of the representations, not the reason the MLP exists. It expands to 4d_model with GELU. 

preLN vs postLN (why did GPT-2 use pre-LN?)



# Masking?
In training masking is used becauase all positions are predicted in parallel, so the mask stops token i from seeing the answer. In inference future tokens don't exist yet, but the mask is kept so earlier tokens representaitons atch training (and so KV caching works)

review ts



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

Applies Learned Scaling and Shifting (gamma and beta)
- gamma is for scaling: multiplies the normalized values to stretch or shrink the variance back to whatever magnitude is optimal for the network.
- beta for shifting: Adds an offset to move the mean wherever the model needs it.

Look into how these parameters are learned during training.

Why is LN important?
- Prevents activation explosion: As numbers pass through dozens of attention and MLP layers, they can rapidly grow in magnitude (or shrink to zero). LayerNorm keeps the scale of the vectors under control.
- Smooths Training. It ensures that no single dimension dominates the vector just because it has larger numbers, making gradient descent much more stable and efficient. 


Attention is all about communication between tokens. It looks across the sequence and lets words pass informatino to each other (making sure the token for "Jordan" knows about "Michael")
MKLPs (Multi-Layer Perceptrons) are all about processing and recall. Because they take each token's vector and run it throug the massively expanded hiddne space (4*d_model), they act like a massive knowledge bank or pattern matcher. 


# Maximum Likelihood Estimation (MLE) in NLPs

MLE is the underlying principle used during training (via gradient descent) to adjust the model's weights so that it assigns higher probabilities to the correct next words that actually appeared in the training corpus and lower probabilities to incorrect words.

At inference, MLE manifests as greedy decoding, or picking the token with the highest probability (arg max).
- Oftentimes results in repetitiveness and dullness. 
- Modern models actually use sampling techniques (like temperature, top-k, or top-p sampling) to introduce a bit of controlled randomness rather than just picking the absolute maximum likelihood token every time. 
- Exposure Bias: Models trained strictly on human-written text using MLE are only ever conditioned on ground truth prefixes. If the model makes a small mistake early in a sentence during generation, it has never seen a sentence with its own mistake before, which can cause it to spiral off-topic.









