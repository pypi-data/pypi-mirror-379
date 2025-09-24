import matplotlib.pyplot as plt

from .set_x_label_prepare_xtick import set_x_label_prepare_xtick
from .setup_y_tick_lim_label_zero_line import setup_y_tick_lim_label_zero_line
from .set_x_tick_and_lim import set_x_tick_and_lim

from mdl.utils_ import get_pos_bot_range_unit_format
from mdl.utils_ import plot_stacked_barchart

def plot_shifted_period_barchart(df_grouped_working_hours_period_unstacked, 
                                          fs=None,
                                          fontsize=None):

    if fs is None:
        fs = (3.51, 3.07)

    plt.style.use('seaborn-v0_8-white')
    fig, ax = plt.subplots(1, 1, figsize=fs)        

    df_grouped_working_hours_period_reset_with_sign = df_grouped_working_hours_period_unstacked.reset_index(drop=True)
    freqstr = df_grouped_working_hours_period_unstacked.index.freqstr

    df_grouped_working_hours_sorted_reset_pos, \
        df_grouped_working_hours_sorted_reset_bot, \
            ylim, \
                display_unit, \
                    formatter = get_pos_bot_range_unit_format(df_grouped_working_hours_period_reset_with_sign, 
                                                                        pad_pct_above_max=0.2)

    setup_y_tick_lim_label_zero_line(ax, ylim, display_unit, formatter, 
                                    freqstr=freqstr,
                                    fontsize=fontsize)

    x_ticks_labels = set_x_label_prepare_xtick(ax, df_grouped_working_hours_period_unstacked,
                                               fontsize=fontsize)

    plot_stacked_barchart(ax, df_grouped_working_hours_sorted_reset_pos, 
                        bottom=df_grouped_working_hours_sorted_reset_bot,
                        tick_range=ylim)

    set_x_tick_and_lim(ax, x_ticks_labels, df_grouped_working_hours_period_unstacked, 
                       fontsize=fontsize)

    fig.tight_layout(rect =(0.01, 0, 1, 1))
    subplots_adjust_left = None
    subplots_adjust_right = 0.68 # 0.92 # 

    fig.subplots_adjust(left=subplots_adjust_left,
                        right=subplots_adjust_right)