
import matplotlib.ticker as ticker

from .get_pos_bot_and_ylim import get_pos_bot_and_ylim

def setup_y_label_and_get_pos_bot_range(ax, df_pivot_working_hours_sorted, 
                                        fontsize=None):

    if fontsize is None:
        fontsize = 13

    df_pivot_working_hours_sorted_reset = df_pivot_working_hours_sorted.reset_index(drop=True)

    df_pivot_working_hours_sorted_reset_pos, \
        df_pivot_working_hours_sorted_reset_bot, \
            ytick_range = get_pos_bot_and_ylim(df_pivot_working_hours_sorted_reset,
                                    pad_pct_above_max = 0.3)

    max_y_tick = max([abs(y_tick) for y_tick in ytick_range])

    if max_y_tick > 0.1: # 100 kwh = 0.1 mwh as switching point for unit as kwh or mwh
        ax.set_ylabel("Daily Usage (MWh)", labelpad=14, fontsize=fontsize)
        
        #ax_l.set_yticks(np.arange(0, tick_range_e, 0.1))
        ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))
    else:
        df_pivot_working_hours_sorted_reset = df_pivot_working_hours_sorted_reset.mul(1000)

        # after the change of units, the dfs and limits should be updated
        df_pivot_working_hours_sorted_reset_pos, \
            df_pivot_working_hours_sorted_reset_bot, \
                ytick_range = get_pos_bot_and_ylim(df_pivot_working_hours_sorted_reset,
                                    pad_pct_above_max = 0.3)

        ax.set_ylabel("Daily Usage (kWh)", labelpad=14, fontsize=fontsize)
        
        #ax_l.set_yticks(np.arange(0, tick_range_e, 0.1))
        ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.0f'))

    return df_pivot_working_hours_sorted_reset_pos, df_pivot_working_hours_sorted_reset_bot, ytick_range