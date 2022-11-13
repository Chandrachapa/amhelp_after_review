
import matplotlib.pyplot as plt

from matplotlib import rc

rc('mathtext', default='regular')
#from matplotlib.ticker import ScalarFormatter
#data
eti = (5,10, 20, 30, 40, 50, 60)
#success_rate_d = (0.71,0.63,0.59,0.48)
success_rate_amhelp = (0.55,0.58,0.6,0.63,0.65,0.66,0.663)
success_rate_mhelp = (0.38,0.44,0.47,0.48,0.49,0.5,0.501)
success_rate_finder = (0.1132,0.255,0.311,0.322,0.34,0.36,0.363,)

success_rate_amhelp10k = (0.55,0.58,0.6,0.63,0.65,0.66,0.663)
success_rate_mhelp10k = (0.38,0.44,0.47,0.48,0.49,0.5,0.501)
success_rate_finder10k = (0.1132,0.255,0.311,0.322,0.34,0.36,0.363,)

success_rate_amhelp5k = ()
success_rate_mhelp5k = ()
success_rate_finder5k = (0.09113012064,0.1639377204,0.2111668703,0.2058573853,0.2181002384,)


arrayY = (0.1,0.2,0.3,0.4,0.5,0.6,0.7)
#arrayD = (0.03, 0.06, 0.14, 0.19,  2.69, 10.13, 15.94, 36.75)

#put labels to all data points
#plt.xticks(t)
# Create a subplots and twin axes
f, ax1 = plt.subplots()


#ax1.fill_between(noc, success_rate_d, success_rate, color='silver', alpha=0.5)
#ax2 = ax1.twinx()
#ax2.plot(time, D_r)
#ax2.plot(time, D_r_1)
#plt.xscale('log', basex=10)
#plt.yscale('log', basey=10)
#limits
ax1.set_ylim(0.08,0.7)
ax1.set_xlim(4,61)
ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)
#ax2.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)
#saving and showing fig

ax1.set_xticks(eti)
ax1.set_xticklabels([5,10, 20, 30, 40, 50, 60], fontsize=10)
ax1.set_yticks(arrayY)
ax1.set_yticklabels([0.1,0.2,0.3,0.4,0.5,0.6,0.7],fontsize=10)

#legend
lns1 = ax1.plot(eti, success_rate_amhelp, color="black",marker="o", label='AM-HELP')
lns2 = ax1.plot(eti, success_rate_mhelp, color="black", marker="*", markersize=7, label='M-HELP')
lns3 = ax1.plot(eti, success_rate_finder, color="black", marker="x",linestyle='--', markersize=7, label='FINDER')

lns = lns1+lns2+lns3
      #+lns3+lns4
labs = [l.get_label() for l in lns]
ax1.legend(lns, labs, loc=4, fontsize=10)

#labels
ax1.set_xlabel("ETI (sec)",fontsize=11)
ax1.set_ylabel(r"success rate", fontsize=11)
#ax2.set_ylabel(r"average messages per node ($D_r$)",fontsize=14)


plt.show()

