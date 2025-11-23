import numpy as np

r = 1
n = 10

A = np.zeros((n,n))
b = np.zeros(n)

for i in range(n):
    A[i,i] = 12*(i+1)
    b[i] = 10.5*np.sqrt(i+1)
    for j in range(n):
        if i!=j:
            A[i,j] = 0.1*((-1)**(i+j))/np.sqrt((i+1)*(j+1))

LU = A.copy()
for k in range(n-1):
    for i in range(k+1,n):
        LU[i,k] /= LU[k,k]
        for j in range(k+1,n):
            LU[i,j] -= LU[i,k]*LU[k,j]

y = np.zeros(n)
for i in range(n):
    s = 0
    for j in range(i):
        s += LU[i,j]*y[j]
    y[i] = (b[i]-s)

x_lu = np.zeros(n)
for i in range(n-1,-1,-1):
    s = 0
    for j in range(i+1,n):
        s += LU[i,j]*x_lu[j]
    x_lu[i] = y[i] - s

res_lu = np.linalg.norm(A@x_lu - b)

x = np.zeros(n)
C = np.zeros((n,n))
d = np.zeros(n)

for i in range(n):
    d[i] = b[i]/A[i,i]
    for j in range(n):
        if i!=j:
            C[i,j] = -A[i,j]/A[i,i]

kmax = 1000
eps = 1e-6

for _ in range(kmax):
    x_old = x.copy()
    for i in range(n):
        s = 0
        for j in range(n):
            if j!=i:
                s += C[i,j]*x[j]
        x[i] = d[i] + s
    if np.linalg.norm(x-x_old) < eps:
        break

res_z = np.linalg.norm(A@x - b)

print("LU:", x_lu, "residual:", res_lu)
print("Seidel:", x, "residual:", res_z)
