
from .group_and_pivot import group_and_pivot
from .transform_asset_stats_for_adaptive_piechart import transform_asset_stats_for_adaptive_piechart

def preprocessing_for_piechart(df_meta_with_value,
                               reading_interval_in_mins=None,
                               asset_group=None,
                               minimum_cnt_for_protection=None,
                                max_display_cnt=None,
                                sum_column=None, 
                                pct_column=None,
                                gene_column=None):

    df_pivot_asset_group_by_period = group_and_pivot(df_meta_with_value, 
                                                    reading_interval_in_mins=reading_interval_in_mins,
                                                    asset_group=asset_group)

    df_sort_idx_trim = transform_asset_stats_for_adaptive_piechart(df_pivot_asset_group_by_period,
                                                                    minimum_cnt_for_protection=minimum_cnt_for_protection,
                                                                    max_display_cnt=max_display_cnt,
                                                                    sum_column=sum_column, 
                                                                    pct_column=pct_column,
                                                                    gene_column=gene_column,
                                                                    asset_group=asset_group)
    
    return df_sort_idx_trim