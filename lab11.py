import numpy as np

a = 1.0
b = 1.0
m = 2
n = 2
beta = 0.3
alpha = np.sqrt(1 - beta**2)
d = 2.0
eps = 1e-6
kmax = 100

def f(x, y):
    return ((alpha*x - beta*y)/a)**m + ((alpha*y + beta*x)/b)**n

def phi_x(x, y):
    return f(x, y_curr)

def phi_y(y, x):
    return f(x_curr, y)

def golden_1d(func, left, right):
    tau = (np.sqrt(5) - 1) / 2
    y = right - tau*(right-left)
    z = left + right - y
    fy = func(y)
    fz = func(z)
    for _ in range(50):
        if abs(right-left) < eps:
            break
        if fy <= fz:
            right = z
            z = y
            fz = fy
            y = right - tau*(right-left)
            fy = func(y)
        else:
            left = y
            y = z
            fy = fz
            z = left + tau*(right-left)
            fz = func(z)
    return (left+right)/2

x_curr = 1.0
y_curr = -0.5

for _ in range(kmax):
    x_old = x_curr
    y_old = y_curr

    x_curr = golden_1d(lambda x: f(x, y_curr), -d, d)
    y_curr = golden_1d(lambda y: f(x_curr, y), -d, d)

    if np.sqrt((x_curr - x_old)**2 + (y_curr - y_old)**2) < eps:
        break

print(x_curr, y_curr)
