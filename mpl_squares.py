import matplotlib.pyplot as plt

input_values: list = [1, 2, 3, 4, 5]
squares: list = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)  # linewidth - толщина линии
# Назначение заголовка диаграммы и меток осей.
plt.title("Square Numbers", fontsize=24)  # title - заголовок диаграммы
# xlabel, ylabel - заголовки каждой из осей
plt.xlabel("Value", fontsize=14)  # fontsize-  размер текста диаграммы
plt.ylabel("Square of Value", fontsize=14)

# Назначение размера шрифта
plt.tick_params(axis='both', labelsize=14)  # axis - деления по обоим осям, с размером шрифта 14
plt.show()
