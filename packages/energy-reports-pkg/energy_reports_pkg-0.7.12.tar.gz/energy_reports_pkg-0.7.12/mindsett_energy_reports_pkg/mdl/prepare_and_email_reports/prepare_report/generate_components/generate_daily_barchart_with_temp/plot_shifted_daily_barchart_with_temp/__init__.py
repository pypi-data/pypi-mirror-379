
import matplotlib.pyplot as plt

from .setup_x_tick_lim import setup_x_tick_lim
from .setup_y_tick_lim_label_zero_line import setup_y_tick_lim_label_zero_line
from .plot_temperature_graph import plot_temperature_graph
from .plot_the_legend import plot_the_legend

from mdl.utils_ import get_pos_bot_range_unit_format
from mdl.utils_ import plot_stacked_barchart


def plot_shifted_daily_barchart_with_temp(df_pivot_working_hours_sorted, 
                                          sr_temp=None,
                                          tick_range_temp=None, 
                                          fs=None,
                                          fontsize=None):

    if fs is None:
        fs = (8, 3.5)
    
    fig, ax = plt.subplots(1, 1, figsize=fs)

    plt.style.use('seaborn-v0_8-white')# set ggplot style

    # df_pivot_working_hours_sorted_reset_pos, \
    # sr_pivot_working_hours_sorted_reset_bot, \
    #     ytick_range = setup_y_label_and_get_pos_bot_range(ax, df_pivot_working_hours_sorted, 
    #                                                     fontsize=fontsize)
    
    df_pivot_working_hours_sorted_reset_pos, \
    sr_pivot_working_hours_sorted_reset_bot, \
        ytick_range, \
             display_unit, \
                 formatter = get_pos_bot_range_unit_format(df_pivot_working_hours_sorted, 
                                                        pad_pct_above_max=0.3)

    # plot the positive part with the bottom line shifted
    plot_stacked_barchart(ax, df_pivot_working_hours_sorted_reset_pos, 
                        bottom=sr_pivot_working_hours_sorted_reset_bot,
                        tick_range=ytick_range)

    # setup x, y tick, limit, label, and zero lines
    setup_x_tick_lim(ax, df_pivot_working_hours_sorted, 
                            fontsize=fontsize)

    # set the layout and adjust if the temperature data exists
    legend_bbox_to_anchor = None # default to: (0.5, 0.99)
    tight_layout_rect = (0, 0, 0.93, 1) # intentionally add some padding on the right hand side
    subplots_adjust_left = None
    subplots_adjust_right = 0.785 # 0.92 # 

    if sr_temp is not None:
        if sr_temp.shape[0] > 0:
            plot_temperature_graph(ax, sr_temp, 
                                fontsize=fontsize, 
                                tick_range=tick_range_temp)
            # tight_layout_rect=(0, 0, 0.94, 1)
            legend_bbox_to_anchor=(0.37, 0.99)
            # subplots_adjust_left = 0.08

    setup_y_tick_lim_label_zero_line(ax, ytick_range, display_unit, formatter,
                            fontsize=fontsize)

    # plot the legend
    plot_the_legend(ax, fontsize=fontsize, 
                    bbox_to_anchor=legend_bbox_to_anchor)

    fig.tight_layout(rect=tight_layout_rect)
    fig.subplots_adjust(left=subplots_adjust_left,
                        right=subplots_adjust_right)