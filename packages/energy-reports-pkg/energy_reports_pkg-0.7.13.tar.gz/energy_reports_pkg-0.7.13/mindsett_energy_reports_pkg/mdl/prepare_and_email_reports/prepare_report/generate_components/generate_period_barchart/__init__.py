import matplotlib.pyplot as plt
import io

from .preprocessing_for_period_barchart import preprocessing_for_period_barchart
from .plot_shifted_period_barchart import plot_shifted_period_barchart


def generate_period_barchart(df_meta_with_value_building,
                            fontsize = None,
                          directory_to_savefig=None):
                          
    df_grouped_working_hours_period_unstacked = preprocessing_for_period_barchart(df_meta_with_value_building)

    # for testing
    # df_grouped_working_hours_period_unstacked[True] = -0.3 * df_grouped_working_hours_period_unstacked[False]
    
    plot_shifted_period_barchart(df_grouped_working_hours_period_unstacked, fontsize=fontsize)

    png_name = 'period_barchart.png'
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