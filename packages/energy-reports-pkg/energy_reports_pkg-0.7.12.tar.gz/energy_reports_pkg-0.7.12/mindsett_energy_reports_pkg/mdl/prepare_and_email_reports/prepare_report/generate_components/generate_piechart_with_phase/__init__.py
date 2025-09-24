
import io
import matplotlib.pyplot as plt


from .preprocessing_for_piechart import preprocessing_for_piechart
from .preprocessing_for_phases import preprocessing_for_phases
from .plot_adaptive_ring_with_phase import plot_adaptive_ring_with_phase


def generate_piechart_with_phase(df_meta_with_value,
                      colors=None,
                      hatches=None,
                      reading_interval_in_mins=None,
                      asset_group=None,
                      minimum_cnt_for_protection=None,
                      max_display_cnt=None,
                      sum_column=None, 
                      pct_column=None,
                      gene_column=None,
                      fontsize=None,
                      directory_to_savefig=None
                      ):

    df_sort_idx_trim = preprocessing_for_piechart(df_meta_with_value,
                                                reading_interval_in_mins=reading_interval_in_mins,
                                                asset_group=asset_group,
                                                minimum_cnt_for_protection=minimum_cnt_for_protection,
                                                    max_display_cnt=max_display_cnt,
                                                    sum_column=sum_column, 
                                                    pct_column=pct_column,
                                                    gene_column=gene_column)
    
    phase_values_list = preprocessing_for_phases(df_meta_with_value,
                                                 reading_interval_in_mins=reading_interval_in_mins)

    plot_adaptive_ring_with_phase(df_sort_idx_trim, phase_values_list,
                                    colors=colors,
                                    hatches=hatches,
                                    sum_column=sum_column, 
                                    pct_column=pct_column,
                                    gene_column=gene_column,
                                    fontsize=fontsize,
                                    )

    png_name = 'consumption_by_assetclass_piechart_with_phase.png'
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