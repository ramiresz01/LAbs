import numpy as np
import plotly.graph_objs as go
import plotly.offline as pyo

# Визначаємо N
n = 24  # Порядковий номер в журналі
N = n + 3

# Функція для симуляції кидання симетричних кубиків
def roll_symmetric_die(N, num_rolls):
    return np.random.randint(1, N + 1, num_rolls)

# Функція для симуляції кидання асиметричного кубика
def roll_asymmetric_die(N, num_rolls):
    return np.random.choice(range(1, N + 1), num_rolls, p=np.arange(1, N + 1) / np.sum(np.arange(1, N + 1)))

# Кількість симуляцій
num_rolls = 10000

# Симуляція для симетричних кубиків
symmetric_die_1 = roll_symmetric_die(N, num_rolls)
symmetric_die_2 = roll_symmetric_die(N, num_rolls)
symmetric_sum = symmetric_die_1 + symmetric_die_2

# Симуляція для одного симетричного та одного асиметричного кубика
asymmetric_die_1 = roll_symmetric_die(N, num_rolls)
asymmetric_die_2 = roll_asymmetric_die(N, num_rolls)
asymmetric_sum = asymmetric_die_1 + asymmetric_die_2

# Створення гістограм
symmetric_hist = np.histogram(symmetric_sum, bins=np.arange(2, 2 * N + 2) - 0.5)
asymmetric_hist = np.histogram(asymmetric_sum, bins=np.arange(2, 2 * N + 2) - 0.5)

# Відображення гістограм за допомогою Plotly
symmetric_trace = go.Bar(x=symmetric_hist[1][:-1], y=symmetric_hist[0], name='Симетричні кубики')
asymmetric_trace = go.Bar(x=asymmetric_hist[1][:-1], y=asymmetric_hist[0], name='Один симетричний та один асиметричний кубик')

data = [symmetric_trace, asymmetric_trace]
layout = go.Layout(title='Гістограма сум результатів кидання двох кубиків',
                   xaxis=dict(title='Сума результатів'),
                   yaxis=dict(title='Частота'),
                   barmode='overlay')

fig = go.Figure(data=data, layout=layout)
fig.update_traces(opacity=0.75)
pyo.plot(fig, filename='dice_simulation_histogram.html')
