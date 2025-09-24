
import numpy as np

def plot_stacked_barchart(ax, df_pivot_working_hours, bottom=None,
                          tick_range=None,
                          top_hours=None):

    if tick_range is None:
        tick_value_e_max = max(0, df_pivot_working_hours.sum(axis=1).max())
        tick_value_e_min = min(0, df_pivot_working_hours.sum(axis=1).min())
        tick_range = [tick_value_e_min, tick_value_e_max]

    if bottom is None:
        bottom = 0
    if top_hours is None:
        top_hours = True

    tick_value_e_var = tick_range[1] - tick_range[0]
    white_padding_below_bar = abs(tick_value_e_var/100)

    bar_padding_adjustment = 0.01 # used when the paddings on the left/right are different
    
    bot_hours = not top_hours

    bar_edgecolour = ['k','w']
    bar_fillcolour = ['k','w']
    bar_color = '#6DC2B3'

    hours_labels = {True: "Out Of Hours", False: "In Hours"}
    hours_colors = {True: "w", False: bar_color}

    # white edge/pad of bar
    ax.bar(df_pivot_working_hours.index, df_pivot_working_hours[top_hours].fillna(0)+df_pivot_working_hours[bot_hours].fillna(0),
           bottom=bottom,
           width=0.7, 
           lw=1.3, 
           edgecolor=bar_edgecolour[0], 
           color=bar_fillcolour[1], 
           label=hours_labels[top_hours])

    # bottom bar inner part
    inner_bar_bot_pad = tick_value_e_var*0.01
    df_white_padding_below_bar_conditional = np.sign(df_pivot_working_hours[bot_hours])*(white_padding_below_bar+inner_bar_bot_pad)
    ax.bar(df_pivot_working_hours.index+bar_padding_adjustment, df_pivot_working_hours[bot_hours].fillna(0) - df_white_padding_below_bar_conditional,
           bottom=bottom+inner_bar_bot_pad,
           width=0.4, 
           lw=0, 
           color= hours_colors[bot_hours], 
           edgecolor=bar_edgecolour[1], 
           label=hours_labels[bot_hours])
