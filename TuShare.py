import matplotlib.pyplot as pit

import tushare as ts

df = ts.get_hist_data('sh', start='2019-01-01')
df.to_excel('stock_sh.xlsx')
df.close.plot()
ax = pit.gca()
ax.invert_xaxis()
pit.show()

