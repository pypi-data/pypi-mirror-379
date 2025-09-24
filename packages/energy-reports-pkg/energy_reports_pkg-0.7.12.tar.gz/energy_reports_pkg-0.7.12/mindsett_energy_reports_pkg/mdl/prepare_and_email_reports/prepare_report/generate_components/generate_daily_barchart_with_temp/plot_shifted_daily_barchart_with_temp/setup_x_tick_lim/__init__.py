
import matplotlib.ticker as ticker

from .generate_day_code import generate_day_code

def setup_x_tick_lim(ax, df_pivot_working_hours_sorted, 
                           fontsize=None):

    if fontsize is None:
        fontsize = 13

    day_code_list = generate_day_code(df_pivot_working_hours_sorted)
    df_pivot_working_hours_sorted_reset = df_pivot_working_hours_sorted.reset_index(drop=True)
        
    # set up the x-ticks and xlim
    ax.tick_params(axis='x', which='major', pad=8, length=2, labelsize=fontsize)

    x_tick_pad =  1.5
    top_index = df_pivot_working_hours_sorted_reset.index.min() - x_tick_pad
    bot_index = df_pivot_working_hours_sorted_reset.index.max() + x_tick_pad
    ax.set_xlim([top_index, bot_index])

    # fixing xticks with matplotlib.ticker "FixedLocator": UserWarning: FixedFormatter should only be used together with FixedLocator
    ticks_loc = ax.get_xticks().tolist()
    ax.xaxis.set_major_locator(ticker.FixedLocator(ticks_loc))
    ax.set_xticklabels(day_code_list, fontsize=fontsize)