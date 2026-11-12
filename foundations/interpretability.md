## Interpretability
Feature directions are indexed by (model checkpoint, layer). Interpretability work is always done on a specific frozen checkpoint at a specific layer. 

Understanding why the model does it by looking inside. Activations, weights, features, circuits, probes, attribution.

Interp work mainly breaks into two things: Features and Circuits.
- Features: what the model represents. This is the direction-finding step (probes, SAEs)
- Circuits: how features are computed from earlier features through the weights, e.g. which heads and MLP neurons turn "Eiffel Tower" plus "is located in" into "Paris"

A list of directions tells you what variables exist; circuits tell you the program uses them. 

The main goal of mechanistic interpretability is to reverse-engineer the algorithm the network implements, so you can explain, predict, and control its behavior. 
- Safety and auditing: check whether a mdoel is deceiving, using a spurious shortcut, or pursuing an unintended goal, instead of trusting its outputs.
- Control: steer or ablate a feature to change behavior (activation steering, model editing) 
- Debugging: find why a specific failure happens
- Science: understand what these models learn at all

You find features per layer, then connect them across layers to get circuits (tools like transcoders, crosscoders, and attribution graphs exist for exactly this). The frozen checkpoint is fine becausae the deployed model is a frozen checkpoint, which is the thing you want to understand. 

Detection deception in models with linear probes and SAEs

# Activation Space vs Weight Space



# Linear Representation Hypothesis



# Superposition



# SAEs 



# VAEs



# Probes
Linear Probes

# Universality Hypothesis
Two models trained with different seeds end up with different directions for the same concept, though often similar ones up to a rotation (the universality hypothesis).