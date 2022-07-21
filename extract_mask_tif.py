# Extract cellpose result as *.tif

import numpy as np
from skimage.io import imsave

############################################ USER INPUT FIELD ##########################################################
filepath = r'X:\Kou\20220624_spheroid\405_bin8\405_bin8_seg.npy'
outputpath = r'X:\Kou\20220624_spheroid\405_bin8\405_bin8_seg.tif'
########################################################################################################################

npy = np.load(filepath, allow_pickle=True).item()
masks = npy['masks']
print(np.shape(masks))
imsave(outputpath, masks)