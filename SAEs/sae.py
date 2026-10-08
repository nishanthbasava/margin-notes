import torch
import torch.nn as nn
import torch.nn.functional as F #bunch of stateless functions

import torch.nn as nn

# This creates an object that internally STORES a 5x10 weight matrix
linear_layer = nn.Linear(in_features=10, out_features=5)

# You can actually see the stored "state" (the weights) inside it:
print(linear_layer.weight) 

#stateless

x = torch.randn(1, 10)
w = torch.randn(5, 10)
b = torch.randn(5) 

output = F.linear(x, w, b)

print(f"x: {x}")
print(f"w: {w}")
print(f"b: {b}")
print(f"Output: {output}")
