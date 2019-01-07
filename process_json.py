import json
import pygal

filename = 'btc_close_2017.json'
with open(filename) as f:
    # 将数据加载到一个列表中
    btc_data = json.load(f)
    # 列表中每个元素都是一个字典
    # for btc_dict in btc_data:
    #     date = btc_dict['date']
    #     month = btc_dict['month']
    #     week = btc_dict['week']
    #     weekday = btc_dict['weekday']
    #     close = btc_dict['close']
    dates, months, weeks, weekdays, close = [], [], [], [], []
    for btc_dict in btc_data:
        dates.append(btc_dict['date'])
        months.append(int(btc_dict['month']))
        weeks.append(int(btc_dict['week']))
        weekdays.append(btc_dict['weekday'])
        # close中的数据为带小数点的字符串，因此只能将其先转换浮点数，再转换成整数
        close.append(int(float(btc_dict['close'])))

# 让x轴上的日期标签顺时针旋转20度，并告诉图形不用显示所有的x轴标签
line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = '收盘价（RMB）'
line_chart.x_labels = dates
# 让x轴坐标每隔20天显示一次
N = 20
line_chart._x_labels_major = dates[::N]
line_chart.add('收盘价', close)
line_chart.render_to_file('收盘价折线图.svg')
