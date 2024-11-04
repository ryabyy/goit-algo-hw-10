import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi
import random

def f(x):
	return x ** 2

a = 0
b = 2

print(f"Definite integral on the range [0, 2]: {8/3:.6f} (Analytical solution [x^3/3 => 8/3 - 0])")
result, error = spi.quad(f, a, b)
print(f"Definite integral on the range [{a}, {b}]: {result:.6f} (SciPy quad)")

n_points = 15000

def is_inside(a, b, x, y):
	return y <= x**2

points = [(random.uniform(a, b), random.uniform(a, b**2)) for _ in range(n_points)]

inside_points = [point for point in points if is_inside(a, b, point[0], point[1])]

N = len(points)
M = len(inside_points)

IMC = (M / N) * (b * b**2)
print(f"Definite integral on the range [{a}, {b}]: {IMC:.6f} (Monte Carlo @ {n_points} pts)")

x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()

ax.plot(x, y, 'r', linewidth=2)

ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Integration graph of f(x) = x^2 from ' + str(a) + ' to ' + str(b))
plt.grid()
plt.show()