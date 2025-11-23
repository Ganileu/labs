import numpy as np

def y_q2(x):
    return np.exp(np.sqrt(x))

def y_q3(x):
    return np.exp(x**(1/3))

def solve_mnk(func, n):
    x = np.linspace(0,1,n+1)
    y = func(x)

    m1 = np.mean(x)
    m2 = np.mean(x**2)
    m3 = np.mean(x**3)
    m4 = np.mean(x**4)

    K01 = np.mean(y)
    K11 = np.mean(x*y)
    K21 = np.mean((x**2)*y)

    A = np.array([
        [1,   m1,  m2],
        [m1,  m2,  m3],
        [m2,  m3,  m4]
    ])
    B = np.array([K01, K11, K21])

    c0, c1, c2 = np.linalg.solve(A,B)
    phi = c0 + c1*x + c2*x**2

    err = np.abs(phi - y)
    return c0, c1, c2, max(err), np.mean(err**2), np.sqrt(np.mean(err**2))

for q, func in [(2,y_q2),(3,y_q3)]:
    for n in [20,40,80]:
        c0,c1,c2,e_max,e_sq,e_rms = solve_mnk(func,n)
        print(q, n, c0, c1, c2, e_max, e_sq, e_rms)
