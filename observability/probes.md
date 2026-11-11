# Linear Probes




Representation Learning: A set of techniques in ML that allows a system to automatically discover the representations (features, patterns, or encodings) needed for feature detection or classification from raw data.

- In deep learning, every hidden layer of a neural network is a representation learning engine. Each layer takes the representaiton from teh previous layer and transforms it into a slightly more abstract, useful space. 

- Supervised Representation Learning: Model learns representations while simultaneously trying to solve a specific task. The internal layesr learn good representations because they are forced to minimize errors on that task.

- Unsupervised / Self-Supervised Representation Learning: Model learns representations of data without human-provided labels. Examples include MLM and Contrastive Learning.

When people say that they are studying "Representations of Deep Learning," they are looking inside the "black box" of a trained model to see how the model has organized information. 

In linear probes, we think that if a model has learned a good representation of language or images, concepts like sentiment, syntax, or object categories will naturally cluster together in its activation space. 

Representation learning is ultimately about finding the "right coordinate system" for complex data so that linear boundaries or simple math can easily make sense of it. 