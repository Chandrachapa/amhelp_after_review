import matplotlib.pyplot as plt

from matplotlib import rc

rc('mathtext', default='regular')
# from matplotlib.ticker import ScalarFormatter
# data
eti = (-95,200,1000,2000,3000,4000,5000)

latency_amhelp = (7,12.23,27.89175633,30.86507394,34.82010757,39.90478531,44.0809768)
latency_mhelp = (10,15.23,41.04090235,47.89261559,48.82891096,52.63979853,59.04092145)
latency_finder = (15,20,96.95322977,105.7242011,123.0451864,128.8252642,145.924647)

arrayY = (15,30,60,80,100,160)

# put labels to all data points

# Create a subplots and twin axes
f, ax1 = plt.subplots()

# limits
#plt.yscale('symlog')
ax1.set_ylim(3, 170)
ax1.set_xlim(-200,5100)
ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)
# saving and showing fig

ax1.set_xticks(eti)
ax1.set_xticklabels([10,100,1000,2000,3000,4000,5000], fontsize=10)
ax1.set_yticks(arrayY)
ax1.set_yticklabels([15,30,60,80,100,160], fontsize=10)

# legend
lns1 = ax1.plot(eti,latency_amhelp, color="black", label='AM-HELP (15k UEs)')
lns2 = ax1.plot(eti, latency_mhelp, color="black", marker="*", markersize=5, label='M-HELP (15k UEs)')
lns3 = ax1.plot(eti, latency_finder, color="black", marker="x", markersize=5, label='FINDER (15k UEs)')
lns = lns1 + lns2 + lns3
labs = [l.get_label() for l in lns]
ax1.legend(lns, labs, fontsize=8,loc='upper center', bbox_to_anchor=(0.5, 1.05),
          ncol=3, fancybox=True, shadow=True)

# labels
ax1.set_xlabel("number of emergency calls", fontsize=11)
ax1.set_ylabel(r"end-end latency (sec)", fontsize=11)
# ax2.set_ylabel(r"average messages per node ($D_r$)",fontsize=14)

plt.show()
