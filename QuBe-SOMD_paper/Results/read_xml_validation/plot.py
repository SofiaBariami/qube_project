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
# fig = plt.figure()

x = [-31.536, -22.1988, -19.0704, -11.721, -7.5942, -4.0962, -1.4775, 2.4251, 7.5014, 9.4081]
y = [-31.536, -22.1988, -19.0704, -11.721, -7.59384, -4.08523, -1.47748, 2.42513, 7.50136 ,9.4081]
n = ["acetic_acid" , "methylacetate" ,"dimethylacetamide" ,"acetaldehyde", "N-methylaniline", "acetophenone", "propane", "bromobenzene" ,"benzene", "benzonitrile"]

plt.style.use('seaborn-whitegrid')

fig, ax = plt.subplots()
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
ax.plot(x,p(x),":", color="silver")
ax.plot(x, y, 'o', color='#34ABC0')
# plt.xlabel('Sire SPE (kcal/mol)')

for i in range(0,len(n)):
    ax.annotate(n[i], (x[i]-0.3, y[i]-1.7))

# the line equation:
print "y=%.6fx+(%.6f)"%(z[0],z[1])
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
ax.set(xlim=(-35, 15), ylim=(-35, 15))
ax.set_xlabel('Sire SPE (kcal/mol)', fontweight='bold')
ax.set_ylabel(' OpenMM SPE (kcal/mol)', fontweight='bold')
fig.suptitle('Sire- OpenMM energies comparison', fontsize=BIGGER_SIZE, fontweight='bold')

# ax.set_title('Sire- OpenMM energies comparison')
plt.show()
