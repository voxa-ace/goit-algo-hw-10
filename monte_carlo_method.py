import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

# Функція для інтегрування
def f(x):
    return x ** 2

# Межі інтегрування
a = 0
b = 2

# Кількість випадкових точок для Монте-Карло
N = 10000

# Генерація випадкових точок
x_rand = np.random.uniform(a, b, N)
y_rand = np.random.uniform(0, f(b), N)

# Порахунок точок під кривою
inside = y_rand < f(x_rand)
inside_sum = np.sum(inside)

# Обчислення інтеграла методом Монте-Карло
integral_mc = (b - a) * f(b) * inside_sum / N

# Аналітичне обчислення інтеграла за допомогою quad
integral_quad, _ = spi.quad(f, a, b)

# Виведення результатів
print(f"Обчислення інтеграла методом Монте-Карло: {integral_mc}")
print(f"Аналітичне обчислення інтеграла (quad): {integral_quad}")

# Візуалізація результатів
plt.scatter(x_rand, y_rand, c='blue', alpha=0.1, marker='.')
plt.plot(np.linspace(a, b, 1000), f(np.linspace(a, b, 1000)), color='red')
plt.fill_between(np.linspace(a, b, 1000), 0, f(np.linspace(a, b, 1000)), color='gray', alpha=0.3)
plt.title("Метод Монте-Карло для обчислення інтеграла")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()
