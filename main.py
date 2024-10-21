import numpy as np
import matplotlib.pyplot as plt


P = np.array([-1.0, -0.5, 0, 0.5, 1.0], dtype=float) # коэффициент корреляции

n = 100

# Генерация стационарных марковских последовательностей для каждого коэффициента корреляции
for phi in P:
    if abs(phi) >= 1:
        print(f"Коэффициент корреляции {phi} не удовлетворяет условию стационарности (|phi| < 1). Пропускаем.")
        continue

    # Генерация белого шума с нулевым средним и единичной дисперсией
    epsilon = np.random.normal(loc=0, scale=1, size=n)

    # Инициализация последовательности
    y = np.zeros(n)

    # Генерация стационарной марковской последовательности
    for t in range(1, n):
        y[t] = phi * y[t-1] + epsilon[t]

    # Построение графика последовательности
    plt.figure(figsize=(10, 4))
    plt.plot(y, label=f'phi = {phi}')
    plt.title(f'Стационарная марковская последовательность для коэффициента корреляции {phi}')
    plt.xlabel('Время')
    plt.ylabel('Значение')
    plt.legend()
    plt.grid(True)
    plt.show()

