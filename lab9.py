import numpy as np

n = 7
p = 3
b = 0.05
r = 0.8
eps = 1e-5
kmax = 1000

A = np.zeros((n,n))

for i in range(n):
    for j in range(n):
        if i == j:
            A[i,j] = 12*(i+1)**(p/3)
        else:
            A[i,j] = b*np.sinh(r/(i+j+2))

x = np.random.rand(n)
x = x/np.max(np.abs(x))

lam_old = 0

for k in range(kmax):
    y = A @ x
    lam = np.max(np.abs(y))
    x = y / lam
    if abs(lam - lam_old) < eps:
        break
    lam_old = lam

print("lambda_max =", lam)
print("eigenvector =", x)
