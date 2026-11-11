## Compression is Intelligence video 1
https://www.youtube.com/watch?v=l6DKRf-fAAM

Perfect Compression is not possible. 

Entropy = average surprise.
Some events are predictable (low surprise), some aren't. 

perfect compression looks like random noise.
- Perfect Compression is where the information content in a message is equal to the number of bits used to encode that message

compression is intelligence.

compression is prediction. 

the pretraining objective is not really about next-token prediction, but instead about creating the most efficient text compressor.


**Entropy measures the average amount of uncertainty, surprise, or information per symbol in a dataset.**

Concretely, it tells you the absolute mathematical lower bound of how many bits are required, on average, to compress that data.

Entropy measures uncertainty in a distribution
But its in units of bits, so lets understand that.
Entropy measures the minimum number of bits per symbol necessary to encode a message following this distribution. 
- Noiseless Coding Theorem

if you treat each new symbol like its being sampled from some probability distribution, those probabilities tell you something about the fundamental limits of compression.

Cross Entropy is like this:
- If you've optimized a compression schema for one context, how does it perform in another context?
- But how do you define/determine optimized? Like there isn't per

Lossless = you can reconstruct the original exactly, bit for bit, fro the compressed version. Nothing is thrown away. (zip, png)
Lossy = you discard some information to shrink further; reconstruction is only approximate (jpeg, mp3)
Shannon's entropy limit H applies to lossless compression. 
You can absolutely go below H, but only by permanently losing information, so you can't recover the original anymore.

Perfect compression = average bits/symbol equals exactly H. 
H is the entropy (sum of the information/surprise of every symbol)

Arithmetic encodign shares fractional bits to get even closer to H, but typically you would only be able to get close to H if the individual informations are integers.
Information = Surprise = Number of bits you need to transmit a message.


## Cross Entropy

Cross entropy is the idea of 

If the probability of each symbol is the same (i.e., they contain the same amount of information/surprise), then regardless of the distribution that we sample from, the
cross entropy will be equal to the entropy.

So basically cross entropy is like, give the optimal code plan for one distribution, what if we applied that plan to another distribution. Then, what would be the new average bits needed, following this same plan.

Cross Entropy is always asking: How well does a code optimized for one setting/distribution, perform in another setting/distribution.
- It is minimized when the distributions are close.

So that's why KL-Divergence measures the change in the distribution.

KL Divergence of P || Q = Cross Entropy (P, Q) - Entropy (P)

Essentially pre-training is just trying to get the model to approach the Entropy of language
