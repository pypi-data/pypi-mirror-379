
from .get_sum_for_curr_and_prev import get_sum_for_curr_and_prev
from .get_subgroup_sum_and_rank import get_subgroup_sum_and_rank
from .get_rank_overall_protect import get_rank_overall_protect
from .get_entries_to_display import get_entries_to_display
from .get_change_pct_and_sort_and_trim_cols import get_change_pct_and_sort_and_trim_cols


def transform_asset_stats_for_adaptive_piechart(df_pivot_asset_group_by_period,
                                                      minimum_cnt_for_protection=None,
                                                      max_display_cnt=None,
                                                      sum_column = None, 
                                                      pct_column = None,
                                                      gene_column=None,
                                                      asset_group=None):

    df_pivot_asset_group_by_period_renamed = get_sum_for_curr_and_prev(df_pivot_asset_group_by_period)
    df_pivot_asset_group_by_period_renamed = get_subgroup_sum_and_rank(df_pivot_asset_group_by_period_renamed)
    df_pivot_asset_group_by_period_renamed_rdx = get_rank_overall_protect(df_pivot_asset_group_by_period_renamed, 
                                                                        minimum_cnt_for_protection=minimum_cnt_for_protection)
    df_pivot_asset_group_by_period_renamed_rdx_to_keep = get_entries_to_display(df_pivot_asset_group_by_period_renamed_rdx,
                                                                                    max_display_cnt=max_display_cnt,
                                                                                    gene_column=gene_column,
                                                                                    asset_group=asset_group)
    df_sort_idx_trim = get_change_pct_and_sort_and_trim_cols(df_pivot_asset_group_by_period_renamed_rdx_to_keep,
                                                sum_column = sum_column, 
                                                pct_column = pct_column,
                                                gene_column = gene_column,
                                                asset_group = asset_group)
    return df_sort_idx_trim