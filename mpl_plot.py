import matplotlib.pyplot as plt

# 横、纵坐标值
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)
# 设置图表标题
plt.title("Square Numbers", fontsize=24)
# 设置坐标轴标签
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square Of Value", fontsize=14)
# 设置刻度标记大小
plt.tick_params(axis='both', labelsize=14)
plt.show()
