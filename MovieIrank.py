import tushare as ts
import matplotlib.pyplot as pit

df = ts.month_boxoffice()
df.to_excel('movie_Feb.xlsx')
# df.close.plot()
ax = pit.gca()
ax.invert_xaxis()
pit.show()
