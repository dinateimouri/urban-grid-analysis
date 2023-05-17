from gridding import apply_gridding_to_user_trajectories
from common_ods_plots import plot_common_origin_destination_statistics
from common_ods_paths import extract_common_origin_destination_paths

dest_directory_address = './griding'
plt_directory_address = './griding'
accuracies = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 30, 40, 50]
city_rec_bbox = [114.153, 38.805, 120.141, 41.677]


apply_gridding_to_user_trajectories(accuracies, city_rec_bbox, dest_directory_address)
plot_common_origin_destination_statistics(accuracies, dest_directory_address, plt_directory_address)
extract_common_origin_destination_paths(accuracies, dest_directory_address)
