import numpy as np

l = 1
m = 1
eps = 1e-6
imax = 30

def f(x):
    return np.exp(-x) - np.sin(np.pi*x/2)

def df(x):
    return -np.exp(-x) - (np.pi/2)*np.cos(np.pi*x/2)

a = 0
b = 1

for i in range(imax):
    c = (a + b) / 2
    if f(a)*f(c) <= 0:
        b = c
    else:
        a = c
    if abs(b - a) < eps:
        break

x_dich = (a + b) / 2

x = 0.2
for i in range(imax):
    x1 = x - f(x)/df(x)
    if abs(x1 - x) < eps:
        break
    x = x1

x_newton = x

print(x_dich)
print(x_newton)
