from pathlib import Path
import matplotlib.pyplot as plt
from datetime import date
import io

from .preprocessing_for_barchart import preprocessing_for_barchart
from .plot_shifted_daily_barchart_with_temp import plot_shifted_daily_barchart_with_temp

def generate_daily_barchart_with_temp(df_meta_with_value, 
                                      sr_temp=None,
                                      fontsize=None, # please note that the other fontsizes haven't been tested yet
                                      directory_to_savefig=None):

    df_pivot_working_hours_sorted, period_current = preprocessing_for_barchart(df_meta_with_value)

    # df_pivot_working_hours_sorted[(True, True)] -= [0.2, 0.1, 0.05, 0.15, 0.08, 0.12, 0.21]
    # df_pivot_working_hours_sorted[(True, False)] -= [0.12, 0.16, 0.08, 0.12, 0.21, 0.05, 0.15]
    # df_pivot_working_hours_sorted[True] = df_pivot_working_hours_sorted[True] *0.5
    # df_pivot_working_hours_sorted[True] -= 0.4*df_pivot_working_hours_sorted[False]

    # df_pivot_working_hours_sorted_reset = df_pivot_working_hours_sorted.reset_index(drop=True)
    # sr_temp = df_pivot_working_hours_sorted_reset[True].sum(axis=1).abs()

    
    plot_shifted_daily_barchart_with_temp(df_pivot_working_hours_sorted,
                                          sr_temp=sr_temp,
                                          fontsize=fontsize)

    png_name = 'daily_barchart_with_temp.png'
    
    if directory_to_savefig == None:
        png_object = io.BytesIO()
        plt.savefig(png_object, format='png', dpi=200)
        plt.close()
        return {png_name: png_object}
    else:
        png_path = directory_to_savefig + png_name
        plt.savefig(png_path, format='png', dpi=200)
        plt.close()
        return {png_name: png_path}
