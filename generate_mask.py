import numpy as np
from skimage.io import imsave
############################################# USER　INPUTS #############################################################
voldim = [501, 1162, 1265]  # The 3D size of your tif. [max(xy), max(xz), max(yz)]
center = [501, 679, 677]  # coordinates: [z, y, x] = [xy, xz, yz]
radius = 343  # radius of the sphere in pixels, on xy plane
pxlsize_x = 3
pxlsize_z = 3
maskName = 'spherical_mask.tif'
########################################################################################################################

[m, n, r] = voldim
x, y, z = np.mgrid[0:m, 0:n, 0:r]
X = x - center[0]
Y = y - center[1]
Z = z - center[2]
mask = X**2 + Y**2 + Z**2 < radius**2

imsave(maskName, mask)