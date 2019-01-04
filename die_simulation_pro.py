from die import Die
from pygal import Bar

die_1 = Die()
# 十面骰子
die_2 = Die(10)
results = []
frequencies = []
for roll in range(10000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = Bar()
hist.title = "Results of rolling a D6 and a D10 10000 times."
# 随着数据的增大，最好利用循环生成x坐标列表
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Result"
hist.y_title = "Frequency of Results"
hist.add("D6+D10", frequencies)
hist.render_to_file("die_simulation_pro.svg")
