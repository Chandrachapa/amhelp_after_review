import matplotlib.pyplot as plt

from matplotlib import rc

rc('mathtext', default='regular')
# from matplotlib.ticker import ScalarFormatter
# data
eti = (600,900,1200,1500,1800)
#success_rate_ahmhelp =(377.412,)
success_rate_amhelp = (0.511,0.524,0.5390862944,0.5538745049,0.5661596823)
success_rate_mhelp = (0.4133342897,0.4185162967,0.4118282102,0.48,0.49)
success_rate_finder = (0.092,0.105,0.1209516194,0.1304,0.14)

#success_rate_amhelp10k = (0.48, 0.49, 0.513, 0.524, 0.54, 0.56, 0.563)
#success_rate_mhelp10k = (0.33, 0.35273211, 0.3702704165, 0.3932106386, 0.4169990433, 0.4451942213, 0.45119003324)
#success_rate_finder10k = (
#0.10113012064, 0.2239377204, 0.2458573853, 0.2611668703, 0.2781002384, 0.28237852455, 0.2868368743)

#success_rate_amhelp5k = (0.39, 0.41, 0.412, 0.424, 0.44, 0.45, 0.453)
#success_rate_mhelp5k = (
#0.2800273211, 0.2900273211, 0.3202704165, 0.3232106386, 0.3769990433, 0.3951942213, 0.4119003324)
#success_rate_finder5k = (
#0.09113012064, 0.1639377204, 0.2058573853, 0.2111668703, 0.2181002384, 0.2237852455, 0.2268368743)

latency_amhelp15k = (75.55474983,73.90209016,74.3404569,74.42954675,74.14180916,73.79240654,73.70945924)
latency_mhelp15k = (112.6533569,106.3295808,111.9138579,110.8661749,112.9127591,118.0075545,122.1508256)
latency_finder15k = (123.6504896,123.6504896,126.8179322,129.9853748,133.1528174,136.3891725,139.4877027)

latency_amhelp10k = ()
latency_finder10k = ()
latency_mhelp10k = ()

latency_amhelp5k = ()
latency_mhelp5k = ()
latency_finder5k = (59.043, 59.7683593, 93.96222378, 95.15357505, 98.08514845, 99.53823033, 138.1712066)

arrayY = (0.1, 0.3, 0.4, 0.5, 0.6)
# arrayD = (0.03, 0.06, 0.14, 0.19,  2.69, 10.13, 15.94, 36.75)

# put labels to all data points
# plt.xticks(t)
# Create a subplots and twin axes
f, ax1 = plt.subplots()

# limits
#plt.yscale('symlog')
ax1.set_ylim(0.05, 0.6)
ax1.set_xlim(598, 1801)
ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)
# ax2.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)
# saving and showing fig

ax1.set_xticks(eti)
ax1.set_xticklabels([600,900,1200,1500,1800], fontsize=10)
ax1.set_yticks(arrayY)
ax1.set_yticklabels([0.1, 0.3, 0.4, 0.5, 0.6], fontsize=10)

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
ax1.set_xlabel("ETI (sec)", fontsize=11)
ax1.set_ylabel(r"success rate", fontsize=11)
# ax2.set_ylabel(r"average messages per node ($D_r$)",fontsize=14)


plt.show()
