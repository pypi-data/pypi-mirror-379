

def get_sum_for_curr_and_prev(df_pivot_asset_group_by_period):

    # get the exact values of current period and period to be compared
    period_range = df_pivot_asset_group_by_period.columns
    period_current = period_range[-1]

    # for avoiding the case that we don't have data for the previous week
    if len(period_range) < 2:
        period_tobe_compared = period_range[-1]
    else:
        period_tobe_compared = period_range[-2]
        
    # get the total of current period and previous period, and the difference between the two periods
    df_pivot_asset_group_by_period_renamed = df_pivot_asset_group_by_period.loc[:,period_current].to_frame().rename(columns={period_current: "sum"})
    df_pivot_asset_group_by_period_renamed["sum_pre"] = df_pivot_asset_group_by_period.loc[:,period_tobe_compared]
    df_pivot_asset_group_by_period_renamed['sub'] = df_pivot_asset_group_by_period.loc[:,period_current] - df_pivot_asset_group_by_period.loc[:,period_tobe_compared]

    return df_pivot_asset_group_by_period_renamed