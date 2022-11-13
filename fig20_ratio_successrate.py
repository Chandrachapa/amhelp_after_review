import matplotlib.pyplot as plt

from matplotlib import rc

rc('mathtext', default='regular')
# from matplotlib.ticker import ScalarFormatter
# data
eti = (1,5,10,30,50,80)

nbm_amhelp = (1,0.9,0.67,0.5099680678,0.4487877695,0.3749307326)
nbm_mhelp = (0.7,0.6,0.52,0.3936323846,0.3538113513,0.2958426036)
nbm_finder = (0.6,0.45,0.2,0.14,0.09866404032,0.08706666667)

arrayY = (0.1,0.3,0.5,0.7,1)

# put labels to all data points

# Create a subplots and twin axes
f, ax1 = plt.subplots()

# limits
#plt.yscale('symlog')
ax1.set_ylim(0.05, 1.05)
ax1.set_xlim(0.8,80.1)
ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)
# saving and showing fig

ax1.set_xticks(eti)
ax1.set_xticklabels([1,5,10,30,50,80], fontsize=10)
ax1.set_yticks(arrayY)
ax1.set_yticklabels([0.1,0.3,0.5,0.7,1], fontsize=10)

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
ax1.set_ylabel(r"success rate ", fontsize=11)
# ax2.set_ylabel(r"average messages per node ($D_r$)",fontsize=14)

plt.show()
