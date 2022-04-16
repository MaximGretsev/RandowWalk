import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Построение случайного блуждания и нанесение точек на диаграмму.

# Новые блуждания строятся до тех пор, пока программа остается активной.
while True:
    rw = RandomWalk(25000)
    rw.fill_walk()

    # Назначение разммера области просмотра
    plt.figure(dpi=128, figsize=(10, 5))
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Reds, s=0.1)
    # plt.plot(rw.x_values, rw.y_values, linewidth=1)

    # Выделение первой и последней точки
    plt.scatter(0, 0, c='yellow', s=20)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='blue', s=20)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
