import numpy as np

A = 2.0
B = 3.0
C = 1.5

a = np.array([1.0, -2.0, 0.5])
b = np.array([1.2, 0.7, 2.5])

N = 2000000

x1 = np.random.uniform(-A, A, N)
x2 = np.random.uniform(-B, B, N)
x3 = np.random.uniform(-C, C, N)

inside = (x1**2/A**2 + x2**2/B**2 + x3**2/C**2) <= 1

xs = np.vstack((x1, x2, x3)).T

rho_vals = np.sum(np.abs(xs - a)**b, axis=1)

W = (2*A)*(2*B)*(2*C)

I = W * np.mean(rho_vals[inside]) * (np.sum(inside)/N)

print(I)
