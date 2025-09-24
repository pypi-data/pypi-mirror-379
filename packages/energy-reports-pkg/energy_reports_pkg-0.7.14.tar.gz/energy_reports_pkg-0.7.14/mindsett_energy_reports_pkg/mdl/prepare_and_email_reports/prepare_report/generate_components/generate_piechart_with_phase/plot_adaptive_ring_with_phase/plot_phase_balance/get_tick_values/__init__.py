
import pandas as pd

def get_tick_values(phase_values_list,
                    min_visible_pct=None):

    if min_visible_pct is None:
        min_visible_pct = 0.077

    df_phase = pd.DataFrame({'phase_value': phase_values_list})

    total_value = df_phase['phase_value'].sum()

    # setup the threshold
    min_visible_value = total_value * min_visible_pct

    # label the visibility
    df_phase['min_visible_value'] = min_visible_value
    df_phase['visible'] = df_phase['phase_value'].gt(min_visible_value)

    # separate by visibility
    df_phase_visible = df_phase.loc[df_phase['visible']]
    df_phase_invisible = df_phase.loc[~df_phase['visible']]

    # get adjusted value for invisible part
    df_phase_invisible['adj_value'] = df_phase_invisible['min_visible_value']

    # get adjusted value for visible part
    compensation = df_phase_invisible['adj_value'].sum() - df_phase_invisible['phase_value'].sum()
    visible_orig_sum = df_phase_visible['phase_value'].sum()
    shrink_pct = (visible_orig_sum - compensation)/visible_orig_sum
    df_phase_visible['adj_value'] = df_phase_visible['phase_value'] * shrink_pct

    # combine the visible and invisible parts back
    df_phase_adj = pd.concat([df_phase_visible, df_phase_invisible]).sort_index()

    # get the tick values
    df_phase_adj['tick_value'] = df_phase_adj['adj_value'].cumsum()

    non_zero_tick_values = df_phase_adj['tick_value'].to_list()

    tick_values_list = [0, *non_zero_tick_values]

    return tick_values_list