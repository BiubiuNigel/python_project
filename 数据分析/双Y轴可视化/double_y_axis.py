
'''
双Y轴可视化产品销量
'''

import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_excel('mrbook.xlsx')

x = [1,2,3,4,5,6]
y1 = df["销量"]
y2 = df["rate"]
fig = plt.figure()
plt.rcParams['font.sans-serif'] = ['SimHei'] #解决中文乱码
plt.rcParams['axes.unicode_minus'] = False #正常显示负号
ax1 = fig.add_subplot(111) #添加子图
plt.title('销售情况对比')

plt.xticks(x,['1月','2月','3月','4月','5月','6月'])
ax1.bar(x,y1,label='left')
ax1.set_ylabel('销量（册）')
#画柱状图的数据
for a,b in zip(x,y1):
    plt.text(a,b,'%.2f'%b,ha='center',va='bottom',fontsize = 10,color = 'black')
ax2 = ax1.twinx() #共享X轴
ax2.plot(x,y2,color='black',linestyle = '--',marker='o',linewidth=2,label=u'增长率')
ax2.set_ylabel(u'增长率')
#画折线图图的数据
for a,b in zip(x,y2):
    plt.text(a, b, '%.2f' % b, ha='center', va='bottom', fontsize=10, color='red')

plt.show()