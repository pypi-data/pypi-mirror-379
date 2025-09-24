

def get_rank_overall_protect(df_pivot_asset_group_by_period_renamed, 
                             minimum_cnt_for_protection=None):

    if minimum_cnt_for_protection is None:
        minimum_cnt_for_protection = 3

    # get the overall ranking considering the minimum entries to protect
    df_pivot_asset_group_by_period_renamed['protect_in_group'] = (df_pivot_asset_group_by_period_renamed['rank_in_group'] <= minimum_cnt_for_protection)
    df_pivot_asset_group_by_period_renamed_rdx = df_pivot_asset_group_by_period_renamed.sort_values(by=['protect_in_group', 'sum_abs'], ascending=False).reset_index()
    df_pivot_asset_group_by_period_renamed_rdx['rank_overall_protect'] = df_pivot_asset_group_by_period_renamed_rdx.index + 1

    return df_pivot_asset_group_by_period_renamed_rdx