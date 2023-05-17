import os
import csv
import pandas as pd
import numpy as np
import transbigdata as tbd


def add_groups(row, params):
    origin = tbd.GPS_to_grid(lon=row['origin_lon'], lat=row['origin_lat'], params=params)
    dest = tbd.GPS_to_grid(lon=row['destination_lon'], lat=row['destination_lat'], params=params)
    return [list(origin), list(dest)]


def apply_gridding_to_user_trajectories(accuracies, city_rec_bbox, dest_directory_address):
    all_data = pd.read_csv(os.path.join(dest_directory_address, 'all_data.csv'))
    grids_params_list = []

    for accuracy in accuracies:
        params_rec_tmp = tbd.area_to_params(city_rec_bbox, accuracy=accuracy, method='rect')
        grids_params_list.append(params_rec_tmp)

        all_data[f'origin_{accuracy}'] = all_data.apply(
            lambda row: list(tbd.GPS_to_grid(lon=row['origin_lon'], lat=row['origin_lat'], params=params_rec_tmp)),
            axis=1)
        all_data[f'destination_{accuracy}'] = all_data.apply(lambda row: list(
            tbd.GPS_to_grid(lon=row['destination_lon'], lat=row['destination_lat'], params=params_rec_tmp)), axis=1)
        all_data[f'group_{accuracy}'] = all_data.apply(lambda row: add_groups(row, params_rec_tmp), axis=1)

    output_data_path = os.path.join(dest_directory_address, 'all_data_gridded.csv')
    all_data.to_csv(output_data_path, index=False)

    grids_params_path = os.path.join(dest_directory_address, 'grids_params.csv')
    with open(grids_params_path, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(grids_params_list)
