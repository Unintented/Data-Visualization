import csv
from matplotlib import pyplot as plt

filename = 'sitka_weather_07-2014.csv'
# 创建一个文件对象，存储在f中
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
    # 阅读器对象从其停留的地方继续向下读取CSV文件，当前是第二行，上方使用过一次next()
    for row in reader:
        high = int(row[1])
        highs.append(high)
    print(highs)

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(highs, c='red')
plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel('Temperature', fontsize=16)
plt.tick_params(axis='both', which='mayor', labelsize=16)
plt.show()
