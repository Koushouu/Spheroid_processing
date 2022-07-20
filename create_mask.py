import numpy as np
voldim = 50
center = [20, 20, 20]
radius = 16  # pixels, in x, y
pxlsize_x = 5
pxlsize_z = 10
vol = np.zeros([voldim, voldim, voldim])

for i in range(voldim):
    for j in range(voldim):
        for k in range(voldim):
            dist2cen = np.sqrt((i-center[0])**2 + (j-center[1])**2 + ((k-center[2])*pxlsize_z/pxlsize_x)**2)
            if dist2cen < radius:
                vol[i, j, k] = 1

from skimage.io import imsave
imsave('test.tif', vol)