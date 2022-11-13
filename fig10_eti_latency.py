import matplotlib.pyplot as plt

from matplotlib import rc

rc('mathtext', default='regular')
# from matplotlib.ticker import ScalarFormatter
# data
eti = (600,900,1200,1500,1800)

latency_amhelp15k = (27.44430091,40.40561377,41.9539261,43.33482183,44.76)
latency_mhelp15k = (18.25849771,44,66.24540739,76,97.2629932)
latency_finder15k = (60.6887326,118.4,119.4755088,128.99,143.9337669)

#latency_amhelp10k = ()
#latency_finder10k = ()
#latency_mhelp10k = ()

#latency_amhelp5k = ()
#latency_mhelp5k = ()
#latency_finder5k = (59.043, 59.7683593, 93.96222378, 95.15357505, 98.08514845, 99.53823033, 138.1712066)

arrayY = (15,30,60,90,120)

# put labels to all data points
# plt.xticks(t)
# Create a subplots and twin axes
f, ax1 = plt.subplots()

# limits
#plt.yscale('symlog')
ax1.set_ylim(16, 150)
ax1.set_xlim(598, 1801)
ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)
# ax2.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)
# saving and showing fig

ax1.set_xticks(eti)
ax1.set_xticklabels([600,900,1200,1500,1800], fontsize=10)
ax1.set_yticks(arrayY)
ax1.set_yticklabels([15,30,60,90,120], fontsize=10)

# legend
lns1 = ax1.plot(eti,latency_amhelp15k, color="black", label='5G SOS (15k UEs)')
lns2 = ax1.plot(eti, latency_mhelp15k, color="black",  linestyle="--", label='M-HELP (15k UEs)')
lns3 = ax1.plot(eti, latency_finder15k, color="black", marker="d",linestyle="dotted", markersize=6, label='FINDER (15k UEs)')
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
ax1.set_xlabel("ETI (sec)", fontsize=11)
ax1.set_ylabel(r"end-end latency (sec)", fontsize=11)
# ax2.set_ylabel(r"average messages per node ($D_r$)",fontsize=14)


plt.show()
