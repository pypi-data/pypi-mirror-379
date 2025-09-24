

def statement_for_total_ooh(df_asset_group_period_sum_others, row_index_for_total='Total', period_freq_str='week'):

    sub_pct_value = df_asset_group_period_sum_others['sub_pct'][row_index_for_total]
    sub_pct_abs_value = round(abs(sub_pct_value * 100))

    if sub_pct_abs_value > 1:
        if sub_pct_value > 0:
            statement_direction = "up"
        else:
            statement_direction = "down"
        statement = f"""The out-of-hours use has gone {statement_direction} by {sub_pct_abs_value}% compared to the {period_freq_str} before.""" #temp fix

    else:   
        statement = f"""The out-of-hours use has been similar to the {period_freq_str} before.""" #temp fix
        
    return statement