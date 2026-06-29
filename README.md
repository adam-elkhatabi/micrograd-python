# Micrograd Implementation

A tiny scalar-valued autograd engine with a small neural network library built on top, implemented in pure Python.

## Core Concepts



1. **The Computational Graph**: Every mathematical operation creates a node.
2. **Backpropagation**: We recursively apply the chain rule starting from the output node to find gradients.

## Quick Start

```python
from micrograd.engine import Value

a = Value(-4.0)
b = Value(2.0)
c = a + b
d = c * b + b**3
c += Value(1.0)
d.backward()

print(f"Gradient of a: {a.grad}") # Prints the derivative dD/da