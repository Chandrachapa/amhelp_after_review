import matplotlib.pyplot as plt

from matplotlib import rc

rc('mathtext', default='regular')
# from matplotlib.ticker import ScalarFormatter
# data
eti = (10,20,30,40,50,60)

latency_amhelp = (40.40561377,52.40004457,55.16000881,62.88060633,69.73794299,79.52300465)
latency_mhelp = (25.01368468,41.01368468,66.24540739,69.61117081,74.85044213,97.2629932)
latency_finder = (76,107,121,131,134,151)

arrayY = (15,30,60,100,160)

# put labels to all data points
# plt.xticks(t)
# Create a subplots and twin axes
f, ax1 = plt.subplots()

# limits
#plt.yscale('symlog')
ax1.set_ylim(13, 170)
ax1.set_xlim(9.9,60.1)
ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)
# ax2.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)
# saving and showing fig

ax1.set_xticks(eti)
ax1.set_xticklabels([10,20,30,40,50,60], fontsize=10)
ax1.set_yticks(arrayY)
ax1.set_yticklabels([15,30,60,100,160], fontsize=10)

# legend
lns1 = ax1.plot(eti,latency_amhelp, color="black", label='5G SOS (15k UEs)')
lns2 = ax1.plot(eti, latency_mhelp, color="black",  linestyle="--", label='M-HELP (15k UEs)')
lns3 = ax1.plot(eti, latency_finder, color="black", marker="d",linestyle="dotted", markersize=6, label='FINDER (15k UEs)')
#lns4 = ax1.plot(eti, success_rate_amhelp10k, color="black", linestyle='--', label='AM-HELP (10k UEs)')
#lns5 = ax1.plot(eti, success_rate_mhelp10k, color="black", marker="*", linestyle='--', markersize=5,
                #label='M-HELP (10k UEs)')
#lns6 = ax1.plot(eti, success_rate_finder10k, color="black", marker="x", linestyle='--', markersize=5,
                #label='FINDER (10k UEs)')
#lns7 = ax1.plot(eti, success_rate_amhelp5k, color="black", linestyle='dotted', label='AM-HELP (5k UEs)')
#lns8 = ax1.plot(eti, success_rate_mhelp5k, color="black", marker="*", markersize=5, linestyle='dotted',
                #label='M-HELP (5k UEs)')
#lns9 = ax1.plot(eti, success_rate_finder5k, color="black", marker="x", linestyle='dotted', markersize=5,
               # label='FINDER (5k UEs)')
lns = lns1 + lns2 + lns3
      #+ lns4 + lns5 + lns6 + lns7 + lns8 + lns9
# +lns3+lns4
labs = [l.get_label() for l in lns]
ax1.legend(lns, labs, fontsize=8,loc='upper center', bbox_to_anchor=(0.5, 1.05),
          ncol=3, fancybox=True, shadow=True)

# labels
ax1.set_xlabel("emergency call transfer duration (sec)", fontsize=11)
ax1.set_ylabel(r"end-end latency (sec)", fontsize=11)
# ax2.set_ylabel(r"average messages per node ($D_r$)",fontsize=14)


plt.show()
