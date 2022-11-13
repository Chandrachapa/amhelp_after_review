import matplotlib.pyplot as plt

from matplotlib import rc

rc('mathtext', default='regular')
# from matplotlib.ticker import ScalarFormatter
# data
eti = (6000,8000,9000,12000,15000)

success_rate_amhelp = (45.82878632,48.16924033,53.7412071,64.65791714,65.5457053)
success_rate_mhelp = (22.65819291,34.2756718,66.24540739,76,97.2629932)
success_rate_finder = (96.95322977,105.7242011,123.0451864,144.6358065,157.6764125)

#latency_amhelp10k = ()
#latency_finder10k = ()
#latency_mhelp10k = ()

#latency_amhelp5k = ()
#latency_mhelp5k = ()
#latency_finder5k = (59.043, 59.7683593, 93.96222378, 95.15357505, 98.08514845, 99.53823033, 138.1712066)

arrayY = (15,30,60,100,160)

# put labels to all data points
# plt.xticks(t)
# Create a subplots and twin axes
f, ax1 = plt.subplots()

# limits
#plt.yscale('symlog')
ax1.set_ylim(13, 180)
ax1.set_xlim(5990,15010)
ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)
# ax2.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)
# saving and showing fig

ax1.set_xticks(eti)
ax1.set_xticklabels([6000,8000,9000,12000,15000], fontsize=10)
ax1.set_yticks(arrayY)
ax1.set_yticklabels([15,30,60,100,160], fontsize=10)

# legend
lns1 = ax1.plot(eti,success_rate_amhelp, color="black", label='5G SOS (15k UEs)')
lns2 = ax1.plot(eti, success_rate_mhelp, color="black",  linestyle="--", label='M-HELP (15k UEs)')
lns3 = ax1.plot(eti, success_rate_finder, color="black", marker="d",linestyle="dotted", markersize=6, label='FINDER (15k UEs)')
lns = lns1 + lns2 + lns3
      #+ lns4 + lns5 + lns6 + lns7 + lns8 + lns9
# +lns3+lns4
labs = [l.get_label() for l in lns]
ax1.legend(lns, labs, fontsize=8,loc='upper center', bbox_to_anchor=(0.5, 1.05),
          ncol=3, fancybox=True, shadow=True)

# labels
ax1.set_xlabel("number of UEs", fontsize=11)
ax1.set_ylabel(r"end-end latency (sec)", fontsize=11)
# ax2.set_ylabel(r"average messages per node ($D_r$)",fontsize=14)


plt.show()
