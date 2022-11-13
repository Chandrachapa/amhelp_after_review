import matplotlib.pyplot as plt

from matplotlib import rc

rc('mathtext', default='regular')
# from matplotlib.ticker import ScalarFormatter
# data
eti = (1000,2000,3000,4000,5000)

nbm_amhelp = (32.71039474,34.15663644,35.29621267,35.40451963,35.75688037)
nbm_mhelp = (25.52495538,26.50765807,26.73406959,26.82711454,27.10110046)
nbm_finder = (38.4,49.2,57.6,86.8,96)

arrayY = (20,35,60,75,100)

# put labels to all data points

# Create a subplots and twin axes
f, ax1 = plt.subplots()

# limits
#plt.yscale('symlog')
ax1.set_ylim(20, 50)
ax1.set_xlim(900,5200)
ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)
# saving and showing fig

ax1.set_xticks(eti)
ax1.set_xticklabels([1000,2000,3000,4000,5000], fontsize=10)
ax1.set_yticks(arrayY)
ax1.set_yticklabels([20,35,60,75,100], fontsize=10)

# legend
lns1 = ax1.plot(eti,nbm_amhelp, color="black", label='AM-HELP (15k UEs)')
lns2 = ax1.plot(eti, nbm_mhelp, color="black", marker="*", markersize=5, label='M-HELP (15k UEs)')
lns3 = ax1.plot(eti, nbm_finder, color="black", marker="x", markersize=5, label='FINDER (15k UEs)')
lns = lns1 + lns2 + lns3
labs = [l.get_label() for l in lns]
ax1.legend(lns, labs, fontsize=8,loc='upper center', bbox_to_anchor=(0.5, 1.05),
          ncol=3, fancybox=True, shadow=True)

# labels
ax1.set_xlabel("number of emergency calls", fontsize=11)
ax1.set_ylabel(r"energy consumption per node (mJ) ", fontsize=11)
# ax2.set_ylabel(r"average messages per node ($D_r$)",fontsize=14)

plt.show()
