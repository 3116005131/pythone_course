import tushare as ts
import matplotlib.pyplot as plt
import matplotlib as mpl

df = ts.realtime_boxoffice()
df.to_excel('movie_realtime.xlsx')

mpl.rcParams['axes.unicode_minus'] = False
mpl.rcParams['font.sans-serif'] = ['SimHei']

explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
figl, ax1 = plt.subplots()
ax1.pie(df['BoxOffice'], explode=explode, labels=df['MovieName'], autopct='%1.1f%%',shadow=True,startangle=90)
ax1.axis('equal')
plt.show()
