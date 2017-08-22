import datetime
import random

import numpy as np
import matplotlib.ticker as mticker
import matplotlib.finance as fin
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.cbook as cbook
from matplotlib import style


#style.use('dark_background')
#style.use('fivethirtyeight')
#print(plt,style.available)
#style.use('ggplot')

#print(plt.__file__)

MA1 = 10
MA2 = 30

def moving_avavrage(values, window):
	weights = np.repeat(1.0, window)/window
	smas = np.convolve(values, weights, 'valid')
	return smas

def high_minus_low(highs, lows):
	return highs - lows


datafile = cbook.get_sample_data('goog.npy')

#date, open, close, volume, adj_close from
r = np.load(datafile, encoding='bytes').view(np.recarray)

fig = plt.figure()

ax = plt.subplot2grid((6,1), (0,0), rowspan=1, colspan=1)
plt.title('Interesting Graph')
plt.ylabel('H-L')
ax1 = plt.subplot2grid((6,1), (1,0), rowspan=4, colspan=1, sharex=ax)
plt.ylabel('Price')
ax1v = ax1.twinx()

ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax)
plt.ylabel('MAvgs')

close = []

def app_close(start_close, new_close):
	g = np.pi/2
	for i in start_close:
		i = i*(np.sin(g))
		g += random.choice([0.05, -0.05])
		new_close.append(i)
	return new_close

app_close(r.adj_close, close)

x = 0
y = len(r.date)
ohlc = []

while x < y:
	append_me = r[x][0].toordinal(), r[x][1], r[x][2], r[x][3], r[x][4], r[x][5]
	ohlc.append(append_me)
	x += 1

ma1 = moving_avavrage(r.adj_close, MA1)
ma2 = moving_avavrage(r.adj_close, MA2)
start = len(r.date[MA2-1:])
h_l = list(map(high_minus_low, r.open, r.close))

ax.plot_date(r.date[-start:], h_l[-start:], '-')

ax.yaxis.set_major_locator(mticker.MaxNLocator(nbins=4, prune='lower'))


fin.candlestick_ohlc(ax1, ohlc[-start:], width=0.4, colorup='g',alpha=0.6, colordown='r')

#ax.plot(r.date, r.adj_close)
#ax.plot(r.date, close)

ax1.yaxis.set_major_locator(mticker.MaxNLocator(nbins=7, prune='upper'))
ax1.grid(True)

"""
ax.plot_date(r.date, close,'-',label='Price', color='c')
ax.plot([], [], linewidth=5, label='loss', color='r', alpha=0.5 )
ax.plot([], [], linewidth=5, label='gain', color='g', alpha=0.5 )
#ax.axhline(close[0], color='k', linewidth=5)#лінія приякомусь значені

ax.fill_between(r.date,
			    close, 
			    close[0],
				where=(close>close[0]), 
				facecolor='g',
				alpha=0.3)

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

ax.grid(True, color='c') # color='g', linestyle='-', linewidth=5)
#ax.xaxis.label.set_color('c')
#ax.yaxis.label.set_color('m')
#440
#ax.set_yticks([0, 300, 600, 900])

ax.spines['left'].set_color('c')
ax.spines['bottom'].set_color('c') 
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
#ax.spines['left'].set_linewidth(5)

ax.tick_params(axis='x', colors='c')
ax.tick_params(axis='y', colors='c')
"""

#ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')
"""
ax.annotate('Bed News', (r[13][0],r[13][2]), 
			xytext=(0.8, 0.9), textcoords='axes fraction', 
			arrowprops=dict(facecolor='grey', color='grey'))


font_dict = {'family':'serif', 
			 'color':'darkred',
			 'size':15}


ax.text(r[10][0].toordinal(), r[1][1], "Text Example",fontdict=font_dict)
"""
ax1v.fill_between(r.date[-start:],0 ,r.volume[-start:], facecolor='c', alpha=0.4)
ax1v.axes.yaxis.set_ticklabels([])
ax1v.grid(False)
ax1v.set_ylim(0, 3*r.volume.max())

bbox_props = dict(boxstyle='round4', fc='w', ec='k', lw=1)

ax.annotate(str(r[-1][1]), (r[-1][0].toordinal(), r[-1][1]),
	xytext = (r[-1][0].toordinal()+4, r[-1][1]), bbox=bbox_props)


ax2.plot(r.date[-start:], ma1[-start:], linewidth=1)
ax2.plot(r.date[-start:], ma2[-start:], linewidth=1)

ax2.fill_between(r.date[-start:], ma2[-start:], ma1[-start:], 
				 where=( ma1[-start:] <  ma2[-start:]),
				 facecolor='r',
				 edgecolor='r', 
				 alpha=0.5)

ax2.fill_between(r.date[-start:], ma2[-start:], ma1[-start:], 
				 where=( ma1[-start:] >  ma2[-start:]),
				 facecolor='g',
				 edgecolor='g', 
				 alpha=0.5)

for label in ax2.xaxis.get_ticklabels():
	label.set_rotation(45)

ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

ax2.xaxis.set_major_locator(mticker.MaxNLocator(10))
ax2.yaxis.set_major_locator(mticker.MaxNLocator(nbins=5, prune='upper'))



#plt.legend()
plt.setp(ax.get_xticklabels(), visible=False)
plt.setp(ax1.get_xticklabels(), visible=False)

plt.subplots_adjust(left=0.15, 
					bottom=0.24, 
					right=0.94, 
					top=0.9, 
					wspace=0.2, 
					hspace=0)

plt.show()  