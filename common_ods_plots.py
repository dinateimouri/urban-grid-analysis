import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def plot_common_origin_destination_statistics(accuracies, dest_directory_address, plt_directory_address):
    all_data = pd.read_csv(os.path.join(dest_directory_address, 'all_data_gridded.csv'))

    for accuracy in accuracies:
        ods = all_data.groupby(['origin_' + str(accuracy), 'destination_' + str(accuracy)]).size().reset_index().rename(
            columns={0: 'count'})
        ods_len = len(ods)
        ods_with_more_than_one_path = ods.loc[(ods['count'] > 1)]
        ods_with_more_than_one_paths_len = len(ods_with_more_than_one_path)
        ods_with_more_than_two_paths = ods.loc[(ods['count'] > 2)]
        ods_with_more_than_two_paths_len = len(ods_with_more_than_two_paths)
        minimum = ods_with_more_than_one_path['count'].min()
        maximum = ods_with_more_than_one_path['count'].max()

        count, bins = np.histogram(ods_with_more_than_one_path['count'], bins=ods_len)
        pdf = count / sum(count)
        cdf = np.cumsum(pdf)

        plt.plot(bins[1:], cdf, color='green', label='CDF')
        plt.grid(visible=True)
        plt.title('Grid size is {} meter(s)'.format(accuracy))
        plt.xlabel('Number of paths: Min ... Max', loc='center', wrap=True)
        plt.ylabel('Cumulative Distribution Function, ODs with more than one path', loc='center', wrap=True)
        line_threshold = float(1 - ods_with_more_than_two_paths_len / ods_with_more_than_one_paths_len)
        plt.axhline(y=line_threshold, color='r', linestyle=':')
        plt.text(0.8 * maximum, line_threshold + 0.1 * (1 - line_threshold),
                 str(ods_with_more_than_two_paths_len) + ' Useful ODs with more than two paths', color='r', wrap=True)
        plt.text(0.8 * maximum, line_threshold + 0.6 * (1 - line_threshold), str(ods_len) + ' Total ODs', wrap=True)
        plt.text(0.8 * maximum, line_threshold + 0.4 * (1 - line_threshold),
                 str(ods_with_more_than_one_paths_len) + ' Total ODs with more than one path', wrap=True)

        plt_name = 'GridSize_{}_CDF'.format(accuracy)
        plt.savefig(os.path.join(plt_directory_address, '{}.png'.format(plt_name)), format='png', dpi=1200)
        plt.grid()
        plt.close()
