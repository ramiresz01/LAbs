import numpy as np
import matplotlib.pyplot as plt

# Визначаємо функцію sinc
def sinc(x):
    return np.sinc(x / np.pi)  # np.sinc в NumPy визначена як sin(pi*x) / (pi*x)

# Визначаємо функцію f(x) = sinc(26x - 1)
def f(x):
    return sinc(26 * x - 1)

# Створюємо масив значень x на проміжку [0, 1]
x_values = np.linspace(0, 1, 500)

# Обчислюємо відповідні значення f(x)
y_values = f(x_values)

# Побудова графіка
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='$f(x) = \\text{sinc}(26x - 1)$')
plt.title('Графік функції $f(x) = \\text{sinc}(26x - 1)$ на проміжку [0, 1]')
plt.xlabel('$x$')
plt.ylabel('$f(x)$')
plt.grid(True)
plt.legend()
plt.show()
