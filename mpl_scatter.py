import matplotlib.pyplot as plt

x_values_1 = [1, 2, 3, 4, 5]
y_values_1 = [1, 4, 9, 16, 25]
# 自动计算数据
x_values_2 = list(range(1, 1001))
y_values_2 = [x ** 2 for x in x_values_2]

# 绘制较多点时，各点轮廓可能会粘连在一起，传递实参edgecolor='none'，可删除数据的轮廓点
# c用来传递颜色参数，此处表示随y值渐变，由浅蓝到深蓝
plt.scatter(x_values_2, y_values_2, c=y_values_2, cmap=plt.cm.Blues, edgecolors='none', s=5)
# 设置图表标题
plt.title("Square Numbers", fontsize=24)
# 设置坐标轴标签
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square Of Value", fontsize=14)
# 设置刻度标记
plt.tick_params(axis='both', which='major', labelsize=14)
# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 1, 1100000])
plt.show()
# 自动保存图表，存储到该文件相同目录
plt.savefig('scatter.png')
