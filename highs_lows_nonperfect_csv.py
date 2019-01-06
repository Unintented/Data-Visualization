import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs, lows, dates = [], [], []
    # 该数据集中有若干天未记录温度数据，因此要特殊处理
    # 此处使用异常处理模块，处理后循环继续
    # 也可使用continue跳过一些数据
    # 或者使用remove()或del删除部分数据
    for row in reader:
        try:
            date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(date, 'missing data')
        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
plt.title("Daily high and low temperatures of Death Vally, 2014", fontsize=24)
fig.autofmt_xdate()
plt.ylabel("Temperature", fontsize=16)
plt.tick_params(axis='both', which='mayor', labelsize=16)
plt.show()
