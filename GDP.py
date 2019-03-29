import tushare as ts
import matplotlib.pyplot as plt
import matplotlib as mpl
# -----------------------------------------------
ax1 = plt.subplot(211)
ax2 = plt.subplot(223)

df = ts.get_gdp_year()
df.to_excel('gdp_year.xlsx')

# fig = plt.figure(figsize=(8, 4))
# ----------------------------------------------------------
plt.style.use('seaborn')

mpl.rcParams['axes.unicode_minus'] = False
mpl.rcParams['font.sans-serif'] = ['SimHei']
# -----------------------------------------------------------
plt.sca(ax1)
plt.plot(df['year'], df['pi'])
plt.plot(df['year'], df['si'])
plt.plot(df['year'], df['ti'])
plt.title('产业生产总值（年度）')
plt.xlabel('日期')
plt.ylabel('产业生产总值(亿元)')
# fig.autofmt_xdate(rotation=45)
plt.legend()
# ---------------------------------------------------------------
plt.sca(ax2)
plt.scatter(df['pi'], df['si'], c='maroon')
plt.title('第一产业与第二产业生产总值的散点图')
plt.xlabel('第一产业生产总值（亿元）')
plt.ylabel('第二产业生产总值（亿元）')
plt.legend()
# ------------------------------------------
plt.show()
