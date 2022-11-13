import matplotlib.pyplot as plt

from matplotlib import rc

rc('mathtext', default='regular')
# from matplotlib.ticker import ScalarFormatter
# data
eti = (10,20,30,40,50,60)

success_rate_amhelp = (0.6353477519,0.6172116397,0.5848962168,0.573,0.571,0.5674560412)
success_rate_mhelp = (0.4199493435,0.4108178364,0.4071662396,0.403866774,0.4027062187,
0.4023663585)
success_rate_finder = (0.158,0.14,0.117,0.08713333333,0.08706666667,0.0858)

arrayY = (0.1, 0.3, 0.4, 0.5, 0.6,0.7)

f, ax1 = plt.subplots()

# limits
#plt.yscale('symlog')
ax1.set_ylim(0.05, 0.63)
ax1.set_xlim(9.9,60.1)
ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)

ax1.set_xticks(eti)
ax1.set_xticklabels([10,20,30,40,50,60], fontsize=10)
ax1.set_yticks(arrayY)
ax1.set_yticklabels([0.1, 0.3, 0.4, 0.5, 0.6,0.7], fontsize=10)

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
ax1.set_xlabel("emergency call transfer duration (sec)", fontsize=11)
ax1.set_ylabel(r"success rate", fontsize=11)
# ax2.set_ylabel(r"average messages per node ($D_r$)",fontsize=14)


plt.show()
