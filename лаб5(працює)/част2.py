import numpy as np
import matplotlib.pyplot as plt
import time

# Функція для вибору згідно з номером у журналі
def select_function(n, x, N):
    if n == 24:
        return 1 - (x - N/2)**2 / (N/2)**2  # Обрана функція з номером 24
    else:
        raise ValueError("Невідомий номер функції")

# Протабулюємо функцію на проміжку [0, 1] з використанням NumPy
def tabulate_function_numpy(n, N):
    start_time = time.time()
    x_values = np.linspace(0, 1, 100)
    y_values = select_function(n, x_values, N)
    end_time = time.time()
    return y_values, end_time - start_time

# Протабулюємо функцію на проміжку [0, 1] звичайним Python
def tabulate_function_python(n, N):
    start_time = time.time()
    x_values = np.linspace(0, 1, 100)
    y_values = [select_function(n, x, N) for x in x_values]
    end_time = time.time()
    return y_values, end_time - start_time

# Вибираємо параметри
n = 24
N = 3

# Табулюємо функцію звичайним Python
y_values_python, time_python = tabulate_function_python(n, N)

# Табулюємо функцію з використанням NumPy
y_values_numpy, time_numpy = tabulate_function_numpy(n, N)

# Порівняємо результати обчислень
print("Час табулювання звичайним Python:", time_python)
print("Час табулювання з використанням NumPy:", time_numpy)

# Побудуємо графіки функцій
x_values = np.linspace(0, 1, 100)
plt.plot(x_values, y_values_python, label='Python')
plt.plot(x_values, y_values_numpy, label='NumPy')
plt.title("Порівняння табулювання функції")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()
