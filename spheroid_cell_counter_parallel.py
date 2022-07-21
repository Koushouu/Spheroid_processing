######################## USER INPUT FIELD ##############################################################################
from skimage.io import imread
import numpy as np
import time
import multiprocessing

seg_result_path = r'X:\Kou\20220624_spheroid\405_bin8\405_bin8_seg.tif'
nano_ptl_path = r'X:\Kou\20220624_spheroid\560_bin8\560_bin8.tif'
n_cpu = 40
result_npy_name = 'cell_stats_parallel'
########################################################################################################################

seg_result = imread(seg_result_path)
nano_ptl = imread(nano_ptl_path)

def cell_stat_extract(i):
    if i % 10 == 0:
        print('Processing ROI = ' + str(i))
    cell_id = i + 1
    cell_loc = np.where(seg_result == cell_id)
    cell_loc_x = np.mean(cell_loc[0])
    cell_loc_y = np.mean(cell_loc[1])
    cell_loc_z = np.mean(cell_loc[2])
    cell_size = len(cell_loc[0])
    nanoptl_int_lst = nano_ptl[cell_loc]
    nanoptl_int = np.mean(nanoptl_int_lst)
    return cell_id, cell_loc_x, cell_loc_y, cell_loc_z, cell_size, nanoptl_int

if __name__ == "__main__":

    # Count number of nuclei
    print('Counting number of identified cells...')
    n_nuclei = np.amax(seg_result)
    print('Number of detected nuclei: ' + str(n_nuclei))
    # Find the size distribution of all segmented nuclei
    print('Computing cell stats...')
    cell_stats = {"cell_id": [],
                  "cell_loc_x": [],
                  "cell_loc_y": [],
                  "cell_loc_z": [],
                  "cell_size": [],
                  "nanoptl_int": []}

    start_time = time.perf_counter()
    pool = multiprocessing.Pool(n_cpu)
    processes = [pool.apply_async(cell_stat_extract, args = (i, )) for i in range(n_nuclei)]
    result = [p.get() for p in processes]
    for i in range(n_nuclei):
        cell_stats["cell_id"].append(result[i][0])
        cell_stats["cell_loc_x"].append(result[i][1])
        cell_stats["cell_loc_y"].append(result[i][2])
        cell_stats["cell_loc_z"].append(result[i][3])
        cell_stats["cell_size"].append(result[i][4])
        cell_stats["nanoptl_int"].append(result[i][5])

    np.save(result_npy_name, cell_stats)

    finish_time = time.perf_counter()
    print(f"Program finished in {finish_time - start_time} seconds")