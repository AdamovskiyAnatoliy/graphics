import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.cbook as cbook


datafile = cbook.get_sample_data('goog.npy')

r = np.load(datafile, encoding='bytes').view(np.recarray)

fig = plt.figure()
ax = plt.subplot2grid((1,1), (0,0))

ax.plot_date(r.date, r.adj_close,'-',label='Price')

for label in ax.xaxis.get_ticklabels():
	label.set_rotation(45)

datemin = datetime.date(r.date.min().year, 1, 1)
datemax = datetime.date(r.date.max().year + 1, 1, 1)
ax.set_xlim(datemin, datemax)

ax.grid(True) # color='g', linestyle='-', linewidth=5)

ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')

plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Interesting Graph')
plt.legend()
plt.subplots_adjust(left=0.09, 
					bottom=0.18, 
					right=0.94, 
					top=0.9, 
					wspace=0.2, 
					hspace=0)

plt.show()