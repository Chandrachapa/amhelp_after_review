import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
from matplotlib.ticker import AutoMinorLocator

rc('mathtext', default='regular')
#from matplotlib.ticker import ScalarFormatter
#data
#15k average apd
time = (121.3333187,
        240.3017934,
        361.7600284,
        481.7971508,
        606.8551306,
        739.4784034,
        841.5119859,
        985.2494326,
        1082.049853,
        1211.674369,
        1324.038277,
        1568.091496,
        1688.091496,
        1801.94405,
        2108.409799)
#success_rate_d = (0.71,0.63,0.59,0.48)
error01 = (185.7008,
           156.4811,
           158.2555,
           157.5713,
           157.3215,
           157.3968,
           157.6167,
           157.8163,
           158.0223,
           158.6764265,
           159.1873046,
           159.2458,
           159.7360,
           159.8113,
           159.7981)
error05 = (190.1277,
           160.6482,
           162.7814,
           161.8039,
           161.7573,
           162.1772,
           163.0792,
           163.1351,
           162.9399,
           163.4933559,
           164.0731735,
           164.2240,
           164.5354,
           164.5687,
           164.6641
         )

error08= (198.8948,
          167.6812,
          170.8892,
          171.1868,
          171.2034,
          171.2891,
          171.9828,
          172.2300,
          172.5352,
          173.1812485,
          173.7739551,
          174.0927,
          174.7388,
          175.0881,
          175.2584
       )
error1=(202.1593,
              171.0289,
              173.6934,
              173.5446,
              173.6144,
              174.2952,
              175.4242,
              175.6143,
              175.9035,
              176.6842227,
              177.3422673,
              177.4659,
              177.9330,
              178.3330,
              178.5143
       )

f, ax1 = plt.subplots()

ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)

#legend
lns1 = ax1.plot(time, error01, color="navy",marker="p", markersize=7, label=r'$\alpha_{rssi}$= $\alpha_{toa}$= 0.1, $a_{AOA}$ = $60^0$ (15k UEs)')
lns2 = ax1.plot(time, error05,color="navy",marker="d",linestyle='dashed', markersize=7,  label=r'$\alpha_{rssi}$= $\alpha_{toa}$= 0.5, $a_{AOA}$ = $60^0$ (15k UEs)')
lns3 = ax1.plot(time, error08,color="navy",marker="*",linestyle='dashed', markersize=7, label=r'$\alpha_{rssi}$= $\alpha_{toa}$= 0.8, $a_{AOA}$ = $60^0$ (15k UEs)')
lns4 = ax1.plot(time, error1, color="navy", marker="s",linestyle='dotted', markersize=7, label=r'$\alpha_{rssi}$= $\alpha_{toa}$= 1, $a_{AOA}$ = $90^0$ (15k UEs)')


#ax1.plot(time,minonlycellular,linestyle='dotted',color="black")
#ax1.plot(time,maxonlycellular,linestyle='dotted',color="black")

#plt.fill_between(time, minonlycellular, maxonlycellular, alpha = .1,color = 'olive')
lns = lns1+lns3+lns4
labs = [l.get_label() for l in lns]

for i in range(len(time)):
    my_selected_date = time[i]
    lnv1 = ax1.vlines(my_selected_date, 0, error1[i]+0.03, linestyles ="dashed", colors ="brown", alpha=0.5,linewidth=1)   # changed
    #lnv2 = ax1.vlines(my_selected_date, 2.51, ekf[i]+0.005, linestyles ="dashed", colors ="orange",alpha=0.9,linewidth=0.5)   # changed
ax1.axvline(x=time[0],ymin=0.0, ymax=0.03 ,label='localization update time',linestyle ="dashed", color ="brown", alpha=1,linewidth=0.5)
#ax1.legend(lns2, labs, loc=1, fontsize=10)
#ax1.legend(loc=4, fontsize=10)
ax1.legend(loc=2, fontsize=10)
import matplotlib.font_manager as font_manager
font = font_manager.FontProperties(family='Arial',
                                   style='normal', size=12)
ax1.legend(prop=font)

d = .015  # how big to make the diagonal lines in axes coordinates

for tick in ax1.get_xticklabels():
    tick.set_fontname("Arial")
for tick in ax1.get_yticklabels():
    tick.set_fontname("Arial")
ax1.set_ylim(140.0, 225)  # most of the data
ax1.tick_params(axis='both', which='major', labelsize=14)
plt.text(1000,152.0,'# emergency devices: 340',fontsize=13,fontname="Arial")
plt.text(1000,145.0,'emergency duration: 30 mins',fontsize=13,fontname="Arial")
plt.xlabel(r"time (sec)",fontname="Arial",fontsize=14)
plt.ylabel(r"average distance error (m)",fontname="Arial",fontsize=14)
ax1.set_title("Average distance error against time" , fontname="Arial", fontsize=14)
plt.show()
