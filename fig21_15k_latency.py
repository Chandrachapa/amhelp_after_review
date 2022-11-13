import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
from matplotlib.ticker import AutoMinorLocator

rc('mathtext', default='regular')
#from matplotlib.ticker import ScalarFormatter
#data
noc = (2,300,1000,2000,3000,4000,5000)
#success_rate_d = (0.79,0.74,0.57,0.43)
success_rate_d = (1,0.9,0.8,0.77,0.7,0.57,0.5)
success_rate = (0.7,0.5, 0.4,0.33,0.33,0.3,0.3)
#D_r = (0.19, 0.14, 0.06, 0.03)
#D_r_1 = (36.75, 15.94, 10.13, 2.69)
arrayY = (0.3,0.33,0.4,0.5,0.57,0.7,0.77,0.8,0.9,1)
#arrayD = (0.03, 0.06, 0.14, 0.19,  2.69, 10.13, 15.94, 36.75)

#put labels to all data points
#plt.xticks(t)
# Create a subplots and twin axes
f, ax1 = plt.subplots()

ax1.plot(noc, success_rate_d)
ax1.plot(noc, success_rate)
#ax1.fill_between(noc, success_rate_d, success_rate, color='silver', alpha=0.5)
#ax2 = ax1.twinx()
#ax2.plot(time, D_r)
#ax2.plot(time, D_r_1)

#plt.xscale('log', basex=10)
#limits
ax1.set_ylim(0.26,1.03)
ax1.set_xlim(0.01,5050)
ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)
#ax2.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)
#saving and showing fig

ax1.set_xticks(noc)
ax1.set_xticklabels([10,150,1000,2000,3000,4000,5000], fontsize=10)
ax1.set_yticks(arrayY)
ax1.set_yticklabels([0.3,0.32,0.4,0.5,0.57,0.7,0.78,0.8,0.9,1], fontsize=10)

#legend
lns1 = ax1.plot(noc, success_rate_d, color="black", label='AM-HELP')
lns2 = ax1.plot(noc, success_rate, color="black", marker="*", markersize=6, label='M-HELP')
#lns3 = ax2.plot(time, D_r, color="black", marker="D", markersize=5, label='Dr: gNB = 8')
#lns4 = ax2.plot(time, D_r_1, color="black", marker="d", markersize=5, label='Dr : gNB = 1')
lns = lns1+lns2
      #+lns3+lns4
labs = [l.get_label() for l in lns]
ax1.legend(lns, labs, loc=1, fontsize=10)

#labels
ax1.set_xlabel("number of emergency calls (NEC)",fontsize=10)
ax1.set_ylabel(r"success rate",fontsize=11)
#ax2.set_ylabel(r"average messages per node (Dr)",fontsize=14)


plt.show()