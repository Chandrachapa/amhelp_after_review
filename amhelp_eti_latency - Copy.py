
import matplotlib.pyplot as plt

from matplotlib import rc
#plt.style.use('seaborn')
rc('mathtext', default='regular')
#from matplotlib.ticker import ScalarFormatter
#data
eti = (5,10, 20, 30, 40, 50, 60)
#success_rate_d = (0.71,0.63,0.59,0.48)
latency_amhelp = (315.5547498,313.9020902,314.3404569,314.4295468,314.1418092,313.7924065,313.7094592)
latency_mhelp = (352.6533569,348.393445,351.6203835,350.5357871,351.8713414,358.2566901,362.7402982)
latency_finder = (363.6504896,363.6504896,366.8179322,369.9853748,373.1528174,376.3891725,379.4877027)

#arrayY = (13,15,45,48,51,54,58,62,66,69,73,76,79)
arrayY = (300,310,320,330,340,350,360,370,380,390)

#put labels to all data points
#plt.xticks(t)
# Create a subplots and twin axes
f, ax1 = plt.subplots()

#plt.xscale('log', basex=10)
#plt.yscale('log', basey=10)

#limits
ax1.set_ylim(310,385)
ax1.set_xlim(3.0,61)
ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)

#saving and showing fig
#plt.yscale('log')
ax1.set_xticks(eti)
ax1.set_xticklabels([5,10, 20, 30, 40, 50, 60], fontsize=10)
ax1.set_yticks(arrayY)
#ax1.set_yticklabels([14,15,48,50,52,54,58,62,66,69,73,76,79],fontsize=10)
ax1.set_yticklabels([300,310,320,330,340,350,360,370,380,390],fontsize=10)

#legend
lns1 = ax1.plot(eti, latency_amhelp, color="black",marker="o", label='AM-HELP')
lns2 = ax1.plot(eti, latency_mhelp, color="black", marker="*", markersize=7, label='M-HELP')
lns3 = ax1.plot(eti, latency_finder, color="black", marker="x",linestyle='--', markersize=7, label='FINDER')
lns = lns1+lns2+lns3
      #+lns3+lns4
labs = [l.get_label() for l in lns]
ax1.legend(lns, labs, loc=7, fontsize=10)

#labels
ax1.set_xlabel("ETI (sec)",fontsize=11)
ax1.set_ylabel(r"avg end-end latency (sec)", fontsize=11)

plt.show()
