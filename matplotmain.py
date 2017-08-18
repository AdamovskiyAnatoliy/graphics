import datetime
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.cbook as cbook


datafile = cbook.get_sample_data('goog.npy')

r = np.load(datafile, encoding='bytes').view(np.recarray)

fig = plt.figure()
ax = plt.subplot2grid((1,1), (0,0))

close = []

def app_close(start_close, new_close):
	g = np.pi/2

	for i in start_close:
		i = i*(np.sin(g))
		g += random.choice([0.05, -0.05])
		new_close.append(i)

	return new_close

app_close(r.adj_close, close)

ax.plot_date(r.date, close,'-',label='Price')
ax.plot([], [], linewidth=5, label='loss', color='r', alpha=0.5 )
ax.plot([], [], linewidth=5, label='gain', color='g', alpha=0.5 )
ax.axhline(close[0], color='k', linewidth=5)#лінія приякомусь значені


ax.fill_between(r.date,
			    close, 
			    close[0],
				where=(close>close[0]), 
				facecolor='g',
				alpha=0.3 )

ax.fill_between(r.date,
			    close, 
			    close[0],
				where=(close<=close[0]), 
				facecolor='r',
				alpha=0.3 )




for label in ax.xaxis.get_ticklabels():
	label.set_rotation(45)

datemin = datetime.date(r.date.min().year, 1, 1)
datemax = datetime.date(r.date.max().year + 1, 1, 1)
ax.set_xlim(datemin, datemax)

ax.grid(True) # color='g', linestyle='-', linewidth=5)
#ax.xaxis.label.set_color('c')
#ax.yaxis.label.set_color('m')
#440
#ax.set_yticks([0, 300, 600, 900])

ax.spines['left'].set_color('c')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_linewidth(5)

ax.tick_params(axis='x', colors='#f06215')




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