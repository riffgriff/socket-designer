import sys

sys.path.append(r"C:\Users\griff\ampscan")

import matplotlib
matplotlib.use('tkagg')
from ampscan import AmpObject
import ampscan
import matplotlib.pyplot as plt

def view_point_cloud(amp_obj, density, color, ax=plt.axes(projection = '3d')):
    xs = []
    ys = []
    zs = []
    counter = 0.0
    total = 1.0
    for i in amp_obj.vert:
        if (counter/total < density):
            xs.append(i[0])
            ys.append(i[1])
            zs.append(i[2])
            counter += 1
        total += 1
    # plt.axis('off')
    # s is for dot size, alpha is for transparency
    ax.scatter(xs, ys, zs, s=3, alpha=0.5, color=color)
    ax.set_aspect("equal")
    return ax

# import warnings
# warnings.filterwarnings('ignore')

# MAIN STARTS HERE

# align the messy one to the clean

clean = AmpObject('stl_file.stl')
messy = AmpObject('residual limb scan 1.stl')

aligned = ampscan.align(messy, clean).m

aligned.dynamicTrim(clean, maxdist=40)
# aligned.planarTrim(height=20)

axes = view_point_cloud(aligned, 0.2, "blue")
# view_point_cloud(clean, 1, "red", ax=axes)
plt.show()

aligned.hc_smooth(n=4)

im = aligned.genIm(out='fh', fh='scan1_test.tiff')

aligned.save('scan_1_processed.stl')








    

