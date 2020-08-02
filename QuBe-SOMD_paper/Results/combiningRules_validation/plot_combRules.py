import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

SMALL_SIZE = 8
MEDIUM_SIZE = 10
BIGGER_SIZE = 14

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=MEDIUM_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=BIGGER_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

# plt.subplots_adjust(hspace=0.1)

gx = [-31.536, -22.1988, -19.0704, -11.7657, -7.5942, -4.0962, -1.4775, 2.4251, 7.5014, 9.4081]
gy = [-31.536, -22.1988, -19.0704, -11.7657, -7.59384, -4.08523, -1.47748, 2.42513, 7.50136 ,9.4081]

a_x = [-31.5116 , -22.1723, -18.8614, -11.721, -7.3487, -3.93338, -1.40288, 2.60204, 7.46188, 9.38863]
a_y = [-31.5116, -22.1723, -18.8614, -11.721 , -7.3487, -3.93338, -1.40288, 2.60204 , 7.46188, 9.38863]

n = ["acetic_acid" , "methylacetate" ,"dimethylacetamide" ,"acetaldehyde", "N-methylaniline", "acetophenone", "propane", "bromobenzene" ,"benzene", "benzonitrile"]

plt.style.use('seaborn-whitegrid')

fig = plt.figure(constrained_layout=False)

ax = fig.add_subplot(2,1,1)
# fig, ax = plt.subplots()
z = np.polyfit(gx, gy, 1)
p = np.poly1d(z)
# plt.subplot(2,1,1)
ax.plot(gx,p(gx),":", color="silver")
ax.plot(gx, gy, 'o', color='lightcoral')
# plt.xlabel('Sire SPE (kcal/mol)')


for i in range(0,len(n)):
    ax.annotate(n[i], (gx[i]-0.3, gy[i]-2.3))

# the line equation:
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
ax.set(xlim=(-35, 15), ylim=(-35, 15))
ax.set_xlabel('Sire SPE (kcal/mol)', fontweight='bold')
ax.set_ylabel('SOMD SPE (kcal/mol)', fontweight='bold')
plt.title('Geomertic Combining Rules', fontweight='bold')

ax2 = fig.add_subplot(2,1,2)
# plt.subplot(2,1,2)
az = np.polyfit(a_x, a_y, 1)
p = np.poly1d(az)
ax2.plot(a_x,p(a_x),":", color="thistle")
ax2.plot(a_x, a_y, 'o', color='crimson')


for i in range(0,len(n)):
    ax2.annotate(n[i], (a_x[i]-0.3, a_y[i]-2.3))

# the line equation:
ax2.axhline(y=0, color='k')
ax2.axvline(x=0, color='k')
ax2.set(xlim=(-35, 15), ylim=(-35, 15))
ax2.set_xlabel('Sire SPE (kcal/mol)', fontweight='bold')
ax2.set_ylabel('SOMD SPE (kcal/mol)', fontweight='bold')
plt.title('Arithmetic Combining Rules', fontweight='bold')

fig.suptitle('Energies Comparison Using Arithmetic and Geomertic Combining Rules', fontsize=BIGGER_SIZE, fontweight='bold')

# ax.set_title('Sire- OpenMM energies comparison')
plt.subplots_adjust(hspace=0.3)
plt.show()
