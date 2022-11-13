import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
from matplotlib.ticker import AutoMinorLocator
import matplotlib.ticker as ticker

from scipy.interpolate import interp1d
rc('mathtext', default='regular')
#from matplotlib.ticker import ScalarFormatter
#data
x = (30,400,1000,2000,3000,4000,5000)
y = [0.04,0.026,0.003,0.001,0.001,0.003,0.005]
y1 = [0.05,0.035,0.0113,0.0114,0.0095,0.008,0.007]
array = [0.001,0.003,0.005,0.008,0.01,0.013,0.035,0.05]
#arrayD = (0.03, 0.06, 0.14, 0.19,  2.69, 10.13, 15.94, 36.75)

#put labels to all data points
#plt.xticks(t)
# Create a subplots and twin axes
f, ax1 = plt.subplots()

ax1.plot(x, y)
ax1.plot(x, y1)
#ax1.fill_between(noc, success_rate_d, success_rate, color='silver', alpha=0.5)
#ax2 = ax1.twinx()
#ax2.plot(time, D_r)
#ax2.plot(time, D_r_1)

plt.yscale('log', basey=10)
#limits
ax1.set_ylim(0.0009,0.055)
ax1.set_xlim(0,5050)
ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)
#ax2.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)
#saving and showing fig

ax1.set_xticks(x)
ax1.set_xticklabels([10,150,1000,2000,3000,4000,5000], fontsize=10)
ax1.set_yticks(array)
ax1.set_yticklabels([0.001,0.003,0.005,0.008,0.01,0.013,0.035,0.05],fontsize=10)
#plt.setp(ax1.get_xticklabels(), rotation=30, horizontalalignment='right', fontsize='7')
#legend
#ax1.yaxis.set_major_locator(ticker.MultipleLocator(6))
lns1 = ax1.plot(x, y, color="black", label='AM-HELP')
lns2 = ax1.plot(x, y1, color="black", marker="*", markersize=6, label='M-HELP')
#lns3 = ax2.plot(time, D_r, color="black", marker="D", markersize=5, label='$D_r$: gNB = 8')
#lns4 = ax2.plot(time, D_r_1, color="black", marker="d", markersize=5, label='$D_r$ : gNB = 1')
lns = lns1+lns2
      #+lns3+lns4
labs = [l.get_label() for l in lns]
ax1.legend(lns, labs, loc=1, fontsize=11)

#labels
ax1.set_xlabel(r"number of emergency calls (NEC)", fontsize=14)
ax1.set_ylabel(r"avg latency/(distance x #success calls) (sec/m)", fontsize=14)
#ax2.set_ylabel(r"average messages per node ($D_r$)",fontsize=14)



plt.show()


