import matplotlib.pyplot as plt

x_values: list = list(range(1, 100))
y_values: list = [x ** 2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, edgecolors='none', s=10)

# Назначение заголовка диаграммы и меток осей
plt.title("Square Numbers", fontsize=14)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Назначение диапазона для каждой оси
# plt.axis([0, 100, 0, 10000])

plt.grid(True)

# Назначение размера шрифта деления на осях
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()