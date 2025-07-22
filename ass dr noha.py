import numpy as np

x1 = 0.2
x2 = 0.4

w11 = np.random.uniform(-0.5, 0.5)
w12 = np.random.uniform(-0.5, 0.5)
w21 = np.random.uniform(-0.5, 0.5)
w22 = np.random.uniform(-0.5, 0.5)

b1 = 0.5
z1 = x1 * w11 + x2 * w21 + b1
z2 = x1 * w12 + x2 * w22 + b1
a1 = np.tanh(z1)
a2 = np.tanh(z2)

w31 = np.random.uniform(-0.5, 0.5)
w32 = np.random.uniform(-0.5, 0.5)

b2 = 0.7

z3 = a1 * w31 + a2 * w32 + b2

output = np.tanh(z3)

print("the output:", output)
