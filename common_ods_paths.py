import os
import pandas as pd


def extract_common_origin_destination_paths(accuracies, dest_directory_address):
    all_data = pd.read_csv(os.path.join(dest_directory_address, 'all_data_gridded.csv'))

    for accuracy in accuracies:
        groups = all_data[f'group_{accuracy}'].unique()

        for idx, group in enumerate(groups):
            df = all_data.loc[(all_data[f'group_{accuracy}'] == group)]

            if len(df) > 2:
                group_output_dir = os.path.join(dest_directory_address, str(accuracy))
                os.makedirs(group_output_dir, exist_ok=True)
                output_file_path = os.path.join(group_output_dir, f'group_{idx}.csv')
                df.to_csv(output_file_path, index=False)
