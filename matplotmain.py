import numpy as np
import matplotlib.ticker as mticker
import matplotlib.finance as fin
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.cbook as cbook


MA1 = 10
MA2 = 30

def moving_avavrage(values, window):
	weights = np.repeat(1.0, window)/window
	smas = np.convolve(values, weights, 'valid')
	return smas

def high_minus_low(highs, lows):
	return highs - lows

def graph_data():

	datafile = cbook.get_sample_data('goog.npy')

	r = np.load(datafile, encoding='bytes').view(np.recarray)

	fig = plt.figure()

	ax1 = plt.subplot2grid((6,1), (0,0), rowspan=1, colspan=1)
	plt.title('Interesting Graph')
	plt.ylabel('H-L')

	ax2 = plt.subplot2grid((6,1), (1,0), rowspan=4, colspan=1, sharex=ax1)
	plt.ylabel('Price')
	ax2v = ax2.twinx()

	ax3 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)
	plt.ylabel('MAvgs')

	close = []

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
	
	ax1.plot_date(r.date[-start:], h_l[-start:], '-', label='H-L', linewidth=1, color='c')
	ax1.yaxis.set_major_locator(mticker.MaxNLocator(nbins=4, prune='lower'))

	fin.candlestick_ohlc(ax2, ohlc[-start:], width=0.4, colorup='g',alpha=0.6, colordown='r')

	ax2.yaxis.set_major_locator(mticker.MaxNLocator(nbins=7, prune='upper'))
	ax2.grid(True)

	ax2v.plot([], [], color='c', alpha=0.4, label='Volume')
	ax2v.fill_between(r.date[-start:],0 ,r.volume[-start:], facecolor='c', alpha=0.4)
	ax2v.axes.yaxis.set_ticklabels([])
	ax2v.grid(False)
	ax2v.set_ylim(0, 3*r.volume.max())

	bbox_props = dict(boxstyle='round4', fc='w', ec='k', lw=1)

	ax1.annotate(str(r[-1][1]), (r[-1][0].toordinal(), r[-1][1]),
		xytext = (r[-1][0].toordinal()+4, r[-1][1]), bbox=bbox_props)


	ax3.plot(r.date[-start:], ma1[-start:], linewidth=1, label=str(MA1)+'MA')
	ax3.plot(r.date[-start:], ma2[-start:], linewidth=1, label=str(MA2)+'MA')

	ax3.fill_between(r.date[-start:], ma2[-start:], ma1[-start:], 
					 where=( ma1[-start:] <  ma2[-start:]),
					 facecolor='r',
					 edgecolor='r', 
					 alpha=0.5)

	ax3.fill_between(r.date[-start:], ma2[-start:], ma1[-start:], 
					 where=( ma1[-start:] >  ma2[-start:]),
					 facecolor='g',
					 edgecolor='g', 
					 alpha=0.5)

	for label in ax3.xaxis.get_ticklabels():
		label.set_rotation(45)

	ax3.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

	ax3.xaxis.set_major_locator(mticker.MaxNLocator(10))
	ax3.yaxis.set_major_locator(mticker.MaxNLocator(nbins=5, prune='upper'))



	plt.setp(ax1.get_xticklabels(), visible=False)
	plt.setp(ax2.get_xticklabels(), visible=False)

	plt.subplots_adjust(left=0.15, 
						bottom=0.24, 
						right=0.94, 
						top=0.9, 
						wspace=0.2, 
						hspace=0)
	
	ax1.legend()
	leg = ax1.legend(loc=9, ncol=2, prop={'size':11})
	leg.get_frame().set_alpha(0.4)
	
	ax2v.legend()
	leg = ax2v.legend(loc=9, ncol=2, prop={'size':11})
	leg.get_frame().set_alpha(0.4)
	
	ax3.legend()
	leg = ax3.legend(loc=9, ncol=2, prop={'size':11})
	leg.get_frame().set_alpha(0.4)

if __name__ == '__main__':
	graph_data()
	plt.show()  