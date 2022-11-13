import matplotlib.pyplot as plt

from matplotlib import rc

rc('mathtext', default='regular')
# from matplotlib.ticker import ScalarFormatter
# data
eti = (6000,8000,9000,12000,15000)

success_rate_amhelp = (0.3749307326,0.43,0.4487877695,0.5099680678,0.5674560412)
success_rate_mhelp = (0.2958426036,0.32,0.3538113513,0.3936323846,0.49)
success_rate_finder = (0.08706666667,0.0858,0.09866404032,0.14,0.158)

arrayY = (0.1, 0.3, 0.4, 0.5, 0.6)

# put labels to all data points
# plt.xticks(t)
# Create a subplots and twin axes
f, ax1 = plt.subplots()

# limits
#plt.yscale('symlog')
ax1.set_ylim(0.05, 0.63)
ax1.set_xlim(5999,15010)
ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)
# ax2.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)
# saving and showing fig

ax1.set_xticks(eti)
ax1.set_xticklabels([6000,8000,9000,12000,15000], fontsize=10)
ax1.set_yticks(arrayY)
ax1.set_yticklabels([0.1, 0.3, 0.4, 0.5, 0.6], fontsize=10)

# legend
lns1 = ax1.plot(eti,success_rate_amhelp, color="black", label='5G SOS (15k UEs)')
lns2 = ax1.plot(eti, success_rate_mhelp, color="black",  linestyle="--", label='M-HELP (15k UEs)')
lns3 = ax1.plot(eti, success_rate_finder, color="black", marker="d",linestyle="dotted", markersize=6, label='FINDER (15k UEs)')
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
ax1.set_xlabel("number of UEs", fontsize=11)
ax1.set_ylabel(r"success rate", fontsize=11)
# ax2.set_ylabel(r"average messages per node ($D_r$)",fontsize=14)


plt.show()
