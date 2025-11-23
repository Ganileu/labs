import numpy as np

def y(x):
    return np.sinh(x**2)

def dy(x):
    return 2*x*np.cosh(x**2)

def d2y(x):
    return 2*np.cosh(x**2) + 4*x**2*np.sinh(x**2)

def solve(n):
    h = 1/n
    x = np.linspace(0,1,n+1)
    Y = y(x)

    dy_num = np.zeros(n+1)
    d2y_num = np.zeros(n+1)

    dy_num[0] = (-3*Y[0] + 4*Y[1] - Y[2])/(2*h)
    d2y_num[0] = (2*Y[0] - 5*Y[1] + 4*Y[2] - Y[3])/(h*h)

    for j in range(1,n):
        dy_num[j] = (Y[j+1] - Y[j-1])/(2*h)
        d2y_num[j] = (Y[j+1] - 2*Y[j] + Y[j-1])/(h*h)

    dy_num[n] = (3*Y[n] - 4*Y[n-1] + Y[n-2])/(2*h)
    d2y_num[n] = (2*Y[n] - 5*Y[n-1] + 4*Y[n-2] - Y[n-3])/(h*h)

    err1 = np.abs(dy(x) - dy_num)
    err2 = np.abs(d2y(x) - d2y_num)

    return (max(err1), np.sqrt(np.mean(err1**2))), \
           (max(err2), np.sqrt(np.mean(err2**2)))

for n in [20,40,80]:
    e1, e2 = solve(n)
    print(n, e1, e2)
