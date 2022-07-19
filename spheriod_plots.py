import numpy as np
import matplotlib.pyplot as plt
##################################### Inputs ###########################################################################
cell_stats_npy = r"C:\Users\OWNER\Documents\2021\volume_parallel_process\cell_stats_parallel_test.npy"
coordname = 'goodcells.csv'
########################################################################################################################
# Load data
cellstats = np.load(cell_stats_npy, allow_pickle=True).item()
# Plot the cell voxel size distribution
plt.hist(cellstats['cell_size'], 80)
plt.show()

# Input the minimum cell voxel size
print('Enter the minimum cell size:')
min_cell_size = int(input())
cells_right_size = np.array(cellstats['cell_size']) > min_cell_size
print('There are ' + str(sum(cells_right_size)) + ' cells with size over the minimum cell size')

# Plot the nano particle intensity distribution
nanoptl_int_array = np.array(cellstats['nanoptl_int'])
nanoptl_int_array = nanoptl_int_array[cells_right_size]
plt.hist(nanoptl_int_array, 80)
plt.show()
print('Enter the intensity threshold:')
int_threshold = int(input())
abv_thr = sum(nanoptl_int_array >= int_threshold)
bel_thr = sum(nanoptl_int_array < int_threshold)
print('There are ' + str(abv_thr) + ' cells above the intensity threshold')
print('And there are ' + str(bel_thr) + ' cells below the intensity threshold')
# Get x y z coordinates of the desired cells
# Logical array of cells with high intensity
cells_right_intensity = np.array(cellstats['nanoptl_int']) > int_threshold
# AND with the logical array of cells with right size
target_cells = np.logical_and(cells_right_intensity, cells_right_size)
# Export x, y, z
x_loc = np.array(cellstats['cell_loc_x'])
x_loc = x_loc[target_cells]
y_loc = np.array(cellstats['cell_loc_y'])
y_loc = y_loc[target_cells]
z_loc = np.array(cellstats['cell_loc_z'])
z_loc = z_loc[target_cells]

coord = np.transpose([x_loc, y_loc, z_loc])
np.savetxt(coordname, coord, delimiter=",")
