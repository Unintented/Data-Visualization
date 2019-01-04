from die import Die
import pygal

die = Die()
results = []
# 模拟1000次掷六面骰子
for roll in range(1000):
    result = die.roll()
    results.append(result)
print(results)

frequencies = []
# 统计每个点数出现的次数
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)

hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times."
# x轴的标签
hist.x_labels = ['1', '2', '3', '4', '5', '6']
# 坐标轴的名称
hist._x_title = "Result"
hist._y_title = "Frequency of Results"
# 将获取到的数据列表加入，并标签为'D6'
hist.add('D6', frequencies)
# 将图表渲染成SVG文件，可在浏览器中打开，具有交互性，数据发生变化，只需刷新网页即可看到变化
hist.render_to_file('die_simulation.svg')
