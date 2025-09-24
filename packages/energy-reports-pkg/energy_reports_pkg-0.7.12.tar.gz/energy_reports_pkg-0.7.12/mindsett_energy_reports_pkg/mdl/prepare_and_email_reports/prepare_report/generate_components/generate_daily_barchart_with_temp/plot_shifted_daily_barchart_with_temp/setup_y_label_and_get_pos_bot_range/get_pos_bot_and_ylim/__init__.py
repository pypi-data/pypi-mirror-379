
def get_pos_bot_and_ylim(df_pivot_working_hours_sorted_reset,
                         pad_pct_above_max = None):

    if pad_pct_above_max is None:
        pad_pct_above_max = 0.2

    # make the index unique for later processing
    df_pivot_working_hours_sorted_reset_pos = df_pivot_working_hours_sorted_reset[False]
    sr_pivot_working_hours_sorted_reset_bot = df_pivot_working_hours_sorted_reset[True].sum(axis=1)

    # get the maximum and minimum values
    zero_line = 0
    tick_value_e_max = max(zero_line, df_pivot_working_hours_sorted_reset.sum(axis=1).max()) # ensure that the 0 line is still showing
    tick_value_e_min = min(zero_line, sr_pivot_working_hours_sorted_reset_bot.min()) # ensure that the 0 line is still showing
    tick_value_e_var = tick_value_e_max - tick_value_e_min

    # add padding to the boundary values to make the range
    
    if abs(tick_value_e_min) > (tick_value_e_max*0.01): # if the abs value of tick_value_e_min is very small, then set zero as the lowest range
        pad_pct_below_min = 0.05
    else:
        pad_pct_below_min = 0

    tick_range_e_max = tick_value_e_max + tick_value_e_var*pad_pct_above_max
    tick_range_e_min = tick_value_e_min - tick_value_e_var*pad_pct_below_min

    ls_ylim = [tick_range_e_min, tick_range_e_max]

    return df_pivot_working_hours_sorted_reset_pos, sr_pivot_working_hours_sorted_reset_bot, ls_ylim