import numpy as np

def Phi(x, m, n):
    return np.abs(x)**m * np.arctan(np.abs(x)**n)

def golden(a, b, eps, m, n):
    kmax = 50
    tau = (np.sqrt(5)-1)/2
    y = b - tau*(b-a)
    z = a + b - y
    fy = Phi(y,m,n)
    fz = Phi(z,m,n)
    for _ in range(kmax):
        if abs(b-a) < eps:
            break
        if fy <= fz:
            b = z
            z = y
            fz = fy
            y = b - tau*(b-a)
            fy = Phi(y,m,n)
        else:
            a = y
            y = z
            fy = fz
            z = a + tau*(b-a)
            fz = Phi(z,m,n)
    return (a+b)/2

x_min = golden(-2, 2, 1e-6, 2, 1)
print(x_min)
