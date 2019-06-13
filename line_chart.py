# -* encoding:utf-8 *-
import matplotlib.pyplot as plt
from pylab import *
import pandas as pd

mpl.rcParams['font.sans-serif'] = ['SimHei']
font_size = 11  # 字体大小
# fig_size = (8, 6) # 图表大小
# 更新字体大小
mpl.rcParams['font.size'] = font_size
# 更新图表大小
# mpl.rcParams['figure.figsize'] = fig_size
data = [25.9, 84.6, 21, 21.8, 36.7, 4, 5.2, 43.7, 0.12292, 94]

index = np.arange(len(data))

plt.plot(data, color='b')
plt.xticks(index,
           (u'母亲节', u'跨界歌王', u'天生是优我', u'欢乐颂2', u'我想和你唱', u'小王子的童话之旅', u'一带一路', u'奇葩说', u'黑龙江回应杜特尔特的小愿望', u'运动就是坚持'))

plt.ylabel(u"话题阅读数")
plt.title(u'top10话题阅读数走势图(单位:亿）')
plt.savefig("a3.png")
plt.show()
