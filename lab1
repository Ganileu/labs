import numpy as np

l = 1
m = 2
a = 0
b = 1
n = 100

h = (b - a) / n
x = np.array([a + i*h for i in range(n+1)])

f = np.exp(-x**l) - np.sin(np.pi * x**m / 2)

f_max = np.max(f)
i_max = np.argmax(f)

f_min = np.min(f)
i_min = np.argmin(f)

f_mean = np.mean(f)
f_sq_mean = np.mean(f**2)
f_rms = np.sqrt(f_sq_mean)

p_plus = np.sum(f > 0)
p_minus = np.sum(f < 0)

r_plus = p_plus / len(f)
r_minus = p_minus / len(f)

print(f_max, i_max)
print(f_min, i_min)
print(f_mean)
print(f_sq_mean)
print(f_rms)
print(r_plus, r_minus)
