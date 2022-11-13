import matplotlib.pyplot as plt

from matplotlib import rc

rc('mathtext', default='regular')
# from matplotlib.ticker import ScalarFormatter
# data
eti = (1,5,10,30,50,80)

nbm_amhelp = (29,32.71039474,34.15663644,35.75688037,37.5,41.2)
nbm_mhelp = (24,25.52495538,26.50765807,27.10110046,28.6,29.2)
nbm_finder = (30,38.4,49.2,96,154,198)

arrayY = (25,50,90,150,200)

# put labels to all data points

# Create a subplots and twin axes
f, ax1 = plt.subplots()

# limits
#plt.yscale('symlog')
ax1.set_ylim(20, 210)
ax1.set_xlim(0.8,80.5)
ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)
# saving and showing fig

ax1.set_xticks(eti)
ax1.set_xticklabels([1,5,10,30,50,80], fontsize=10)
ax1.set_yticks(arrayY)
ax1.set_yticklabels([25,50,90,150,200], fontsize=10)

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
ax1.set_ylabel(r"energy consumption per node ", fontsize=11)
# ax2.set_ylabel(r"average messages per node ($D_r$)",fontsize=14)

plt.show()
