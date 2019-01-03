from random_walk import RandomWalk
import matplotlib.pyplot as plt

# 只要回复非n，就不断地模拟随机漫步
while True:
    # 创建一个实例并运行,默认点为5000个
    random_walk_1 = RandomWalk()
    random_walk_1.fill_walk()

    point_nums = list(range(random_walk_1.num_points))
    # 根据漫步的顺序由浅至深着色
    plt.scatter(random_walk_1.x_values, random_walk_1.y_values, c=point_nums, cmap=plt.cm.Blues, s=5, edgecolors='none')
    # 特别标志起始点
    plt.scatter(0, 0, c='black', s=20)
    plt.scatter(random_walk_1.x_values[-1], random_walk_1.y_values[-1], c='red', s=20)

    plt.show()

    keep_running = input("Wanna another random walk?(y/n)")
    if keep_running == 'n':
        break
