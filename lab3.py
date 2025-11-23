import numpy as np

a = 4
b = 3
n = 20
h = 1/n

def y(x):
    return a*x**4 - b*x**3

x = np.array([j*h for j in range(n+1)])
y_vals = y(x)

d1 = (y_vals[1:] - y_vals[:-1]) / h
d2 = (y_vals[2:] - 2*y_vals[1:-1] + y_vals[:-2]) / (2*h*h)

x_half = np.array([(j+0.5)*h for j in range(n-1)])
P = []
err = []

for j in range(n-1):
    xh = x_half[j]
    Pj = y_vals[j] + (xh-x[j])*d1[j] + (xh-x[j])*(xh-x[j+1])*d2[j]
    P.append(Pj)
    err.append(abs(y(xh) - Pj))

print(max(err), np.mean(np.array(err)**2), np.sqrt(np.mean(np.array(err)**2)))
