import numpy as np
import matplotlib.pyplot as plt

# Функція для вибору згідно з номером у журналі
def select_function(n, x):
    if n == 24:
        return 1 - (x - 3/2)**2 / (3/2)**2  # Обрана функція з номером 24
    else:
        raise ValueError("Невідомий номер функції")

# Протабулюємо функцію на проміжку [0, 1]
x_values = np.linspace(0, 1, 100)
y_values = select_function(24, x_values)

# Побудуємо графік функції
plt.plot(x_values, y_values)
plt.title("Графік функції")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.show()
