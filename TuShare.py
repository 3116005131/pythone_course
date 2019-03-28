import matplotlib.pyplot as plt

import tushare as ts

import matplotlib as mpl

# myfont = mpl.font_manager.FontProperties(fname=r"simkai.ttf")

mpl.rcParams['axes.unicode_minus'] = False
mpl.rcParams['font.sans-serif'] = ['SimHei']

plt.style.use('ggplot')

ax1 = plt.subplot(221)
ax2 = plt.subplot(222)
ax3 = plt.subplot(223)
ax4 = plt.subplot(224)

df = ts.get_hist_data('sh', start='2019-01-01')
df.to_excel('stock_sh.xlsx')
plt.sca(ax1)
# plt.legend('s')
plt.title('上证指数')
# plt.xlabel('日期')
plt.ylabel('开盘价')
df.close.plot(lw=2, color='#FF0000', linestyle='-')  # , marker='D')
ax = plt.gca()
ax.invert_xaxis()

dg = ts.get_hist_data('sz', start='2019-01-01')
dg.to_excel('stock_sz.xlsx')
plt.sca(ax2)
# plt.legend('s')
plt.title('深圳成指')
# plt.xlabel('日期')
plt.ylabel('开盘价')
dg.close.plot(lw=2, color='#FF0000', linestyle='-')  # , marker='D')
ax = plt.gca()
ax.invert_xaxis()

dh = ts.get_hist_data('zxb', start='2019-01-01')
dh.to_excel('stock_zxb.xlsx')
plt.sca(ax3)
# plt.legend('s')
plt.title('中小板指数')
# plt.xlabel('日期')
plt.ylabel('开盘价')
dh.close.plot(lw=2, color='#FF0000', linestyle='-')  # , marker='D')
ax = plt.gca()
ax.invert_xaxis()

df = ts.get_hist_data('cyb', start='2019-01-01')
df.to_excel('stock_cyb.xlsx')
plt.sca(ax4)
# plt.legend('s')
plt.title('创业板指数')
# plt.xlabel('日期')
plt.ylabel('开盘价')
df.close.plot(lw=2, color='#FF0000', linestyle='-')  # , marker='D')
ax = plt.gca()
ax.invert_xaxis()

# plt.legend('s')
# plt.title('上证指数')
# plt.xlabel('日期')
# plt.ylabel('开盘价')

# plt.annotate('可在此添加标注', xy=(2700, 2019 - 1 - 24), xytext=(2900, 2019 - 1 - 26), arrowprops=dict(facecolor='black'))

plt.show()
