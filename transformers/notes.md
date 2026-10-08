## Transformers Notes

A GPT (Generative Pre-Trained Transformer) does one thing: given a sequence of tokens, it predicts the next token at every position.

The residual stream.
Each position carries a vector of size d_model from the embedding to the output, and no layer ever replaces it. Every attention layer and MLP reads the stream, computes something, and adds its result back. Two kinds of layers do different jobs:

- Attention is the only place where information moves between positions
- The MLP processes each position independently.

The other pieces are support:
- Layer norm keeps the stream at a stable scale so a deep stack trains.
- The casual mask prevents position t from seeing later positions, so the model can train on every position at once.
- Autoregressive generation is running the model, sampling a token from the last position's output, appending it, and repeating
- The KV cache makes the loop cheap by not recomputing the past

