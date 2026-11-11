## Important Concepts to know

KV Cache
A crucial optimization technique used during text generation (inference). Prevents the model from redundantly recomputing the keys and values for tokens it has already processed.

How Transformers Process Text:
- Tokenization: Input text is broken down into tokens (words or pieces of words)
- Attention Mechanism: For every new token the model generates, it implements self-attention (calculates Query, Keys, Values) matrices via learned weight multiplications
- Autoregressive Generation

During training, the model learns three distinct sets of weights from each attention head:
- Query Weight Matrix (W_q): Transforms the input to see what each token is "looking for"
- Key Weight Matrix (W_k): Transforms the input to describe what information each token "contains" (acting like an indec or label)
- Value Weight Matrix (W_v): Transforms the input to hold the actual "content" that will be pulled if there is a match

KV Cache is exclusively used during inference.
- During training, the model processes entire sequences all at once (in parallel) using a technique called teacher forcing. Because the full sequence is processed together, the model computes the attention across all tokens simultaneously, and there is no need to cache past states
- During inference: The model generates tokens one by one autoregressively. Without a KV cache, it would waste massive amounts of compute time recalculating the Key and Value vectors for all previous tokens at every single step. Caching them allows the model to instantly reuse those past calculations and only compute the vector for the brand-new token. 
