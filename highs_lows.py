# csv模块可用于分析CSV文件中的数据行，可快速提取感兴趣的值
import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'sitka_weather_2014.csv'
# 创建一个文件对象，存储在f中
# 此处一定要注意，下方的两个for循环一定要缩进，即在with语句块中！！！
# 否则文件就会被关闭
with open(filename) as f:
    # 将文件对象作为实参，创建一个与该文件相关联的阅读器对象，存储在reader中
    reader = csv.reader(f)
    # next函数返回文件的下一行
    header_row = next(reader)
    # print(header_row)

    # 函数enumrate获取可遍历的数据对象(如列表、元组)中每个元素的索引(可理解为固有下标，可通过索引随机访问)和值
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    highs = []
    lows = []
    dates = []
    # 阅读器对象从其停留的地方继续向下读取CSV文件，当前是第二行，上方使用过一次next()
    for row in reader:
        # 获取日期及最高温度和最低温度
        current_data = datetime.strptime(row[0], "%Y-%m-%d")
        high = int(row[1])
        low = int(row[3])
        dates.append(current_data)
        highs.append(high)
        lows.append(low)
    print(highs)
    print(lows)
    print(dates)

fig = plt.figure(dpi=128, figsize=(10, 6))
# 显示多个数据系列，alpha表示透明度
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
# facecolor制定了填充区域的颜色
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
plt.title("Daily high and low temperatures, July 2014", fontsize=24)
plt.xlabel('', fontsize=16)
# 绘制斜的日期标签，以免重叠
fig.autofmt_xdate()
plt.ylabel('Temperature', fontsize=16)
plt.tick_params(axis='both', which='mayor', labelsize=16)
plt.show()
