from pandas import read_csv
from matplotlib import pyplot

series = read_csv("USD_BRL_hist.csv", header=0, index_col=0, parse_dates=True, squeeze=True)
series.plot()
pyplot.show()