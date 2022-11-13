import matplotlib.pyplot as plt

from matplotlib import rc

rc('mathtext', default='regular')
# from matplotlib.ticker import ScalarFormatter
# data
eti = (-95,200,1000,2000,3000,4000,5000)

success_rate_amhelp = (1,0.9,0.7606111111,0.71267581,0.6729360502,0.6093314998,0.5674560412)
success_rate_mhelp = (0.7,0.6,0.5798645799,0.4832861347,0.4623643971,0.419971904,0.4091582769)
success_rate_finder = (0.6,0.45,0.2,0.19,0.17,0.16,0.158)

arrayY = (0.1,0.3,0.5,0.7,0.8,0.9,1)

f, ax1 = plt.subplots()

# limits
#plt.yscale('symlog')
ax1.set_ylim(0.05, 1.1)
ax1.set_xlim(-250,5100)
ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)

ax1.set_xticks(eti)
ax1.set_xticklabels([10,100,1000,2000,3000,4000,5000], fontsize=10)
ax1.set_yticks(arrayY)
ax1.set_yticklabels([0.1,0.3,0.5,0.7,0.8,0.9,1], fontsize=10)

# legend
lns1 = ax1.plot(eti, success_rate_amhelp, color="black", label='AM-HELP (15k UEs)')
lns2 = ax1.plot(eti, success_rate_mhelp, color="black", marker="*", markersize=5, label='M-HELP (15k UEs)')
lns3 = ax1.plot(eti, success_rate_finder, color="black", marker="x", markersize=5, label='FINDER (15k UEs)')
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
ax1.set_xlabel("number of emergency calls", fontsize=11)
ax1.set_ylabel(r"success rate", fontsize=11)
# ax2.set_ylabel(r"average messages per node ($D_r$)",fontsize=14)


plt.show()
