import matplotlib.pyplot as plt

from matplotlib import rc

rc('mathtext', default='regular')
# from matplotlib.ticker import ScalarFormatter
# data
eti = (1,5,10,30,50,80)

nbm_amhelp = (7,12.23,24,39.90478531,53.7412071,45.82878632)
nbm_mhelp = (10,15.23,31,52.63979853,66.24540739,72.65819291)
nbm_finder = (15,20,63,96.95322977,123.0451864,128.8252642)

arrayY = (5,20,60,75,130)

# put labels to all data points

# Create a subplots and twin axes
f, ax1 = plt.subplots()

# limits

ax1.set_ylim(7, 140)
ax1.set_xlim(0.8,80.1)
ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)
# saving and showing fig

ax1.set_xticks(eti)
ax1.set_xticklabels([1,5,10,30,50,80], fontsize=10)
ax1.set_yticks(arrayY)
ax1.set_yticklabels([5,20,60,75,130], fontsize=10)

# legend
lns1 = ax1.plot(eti,nbm_amhelp, color="black", label='5G SOS (15k UEs)')
lns2 = ax1.plot(eti, nbm_mhelp, color="black",  linestyle="--", label='M-HELP (15k UEs)')
lns3 = ax1.plot(eti, nbm_finder, color="black", marker="d",linestyle="dotted", markersize=6, label='FINDER (15k UEs)')
lns = lns1 + lns2 + lns3
labs = [l.get_label() for l in lns]
ax1.legend(lns, labs, fontsize=8,loc='upper center', bbox_to_anchor=(0.5, 1.05),
          ncol=3, fancybox=True, shadow=True)

# labels
ax1.set_xlabel("% of emergency calls/number of UEs", fontsize=11)
ax1.set_ylabel(r"end-end latency (sec)", fontsize=11)
# ax2.set_ylabel(r"average messages per node ($D_r$)",fontsize=14)

plt.show()
