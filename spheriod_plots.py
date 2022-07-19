import numpy as np
import matplotlib.pyplot as plt
##################################### Inputs ###########################################################################
cell_stats_npy = r"C:\Users\OWNER\Documents\2021\volume_parallel_process\cell_stats_parallel_test.npy"
########################################################################################################################
# Load data
cellstats = np.load(cell_stats_npy, allow_pickle=True).item()
# Plot the cell voxel size distribution
plt.hist(cellstats['cell_size'], 80)
plt.show()
# Input the minimum cell voxel size
print('Enter the minimum cell size:')
min_cell_size = int(input())
actual_cells = np.array(cellstats['cell_size']) > min_cell_size
print('There are ' + str(sum(actual_cells)) + ' cells with size over the minimum cell size')
# Plot the nano particle intensity distribution
nanoptl_int_array = np.array(cellstats['nanoptl_int'])
nanoptl_int_array = nanoptl_int_array[actual_cells]
plt.hist(nanoptl_int_array, 80)
plt.show()
print('Enter the intensity threshold:')
int_threshold = int(input())
abv_thr = sum(nanoptl_int_array >= int_threshold)
bel_thr = sum(nanoptl_int_array < int_threshold)
print('There are ' + str(abv_thr) + ' cells above the intensity threshold')
print('And there are ' + str(bel_thr) + ' cells below the intensity threshold')


