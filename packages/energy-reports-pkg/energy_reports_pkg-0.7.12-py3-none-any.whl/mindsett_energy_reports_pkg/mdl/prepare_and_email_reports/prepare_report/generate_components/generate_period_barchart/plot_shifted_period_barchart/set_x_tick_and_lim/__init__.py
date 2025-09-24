import matplotlib.ticker as ticker

def set_x_tick_and_lim(ax, x_ticks_labels, df_pivot_working_hours_sorted,
                       fontsize=None):

    if fontsize is None:
        fontsize = 13

    df_pivot_working_hours_sorted_reset = df_pivot_working_hours_sorted.reset_index(drop=True)

    # set up the x-ticks and xlim
    ax.tick_params(axis='x', which='major', pad=8, length=2, labelsize=fontsize)

    x_tick_pad =  0.99
    top_index = df_pivot_working_hours_sorted_reset.index.min() - x_tick_pad
    bot_index = df_pivot_working_hours_sorted_reset.index.max() + x_tick_pad
    ax.set_xlim([top_index, bot_index])

    # used to handle the below warning:
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1)) # ValueError: The number of FixedLocator locations (5), usually from a call to set_ticks, does not match the number of labels (8).

    # fixing yticks with matplotlib.ticker "FixedLocator": UserWarning: FixedFormatter should only be used together with FixedLocator
    ticks_loc = ax.get_xticks().tolist()
    # print(f'{ticks_loc = }')
    ax.xaxis.set_major_locator(ticker.FixedLocator(ticks_loc))
    ax.set_xticklabels(x_ticks_labels, fontsize=fontsize)   