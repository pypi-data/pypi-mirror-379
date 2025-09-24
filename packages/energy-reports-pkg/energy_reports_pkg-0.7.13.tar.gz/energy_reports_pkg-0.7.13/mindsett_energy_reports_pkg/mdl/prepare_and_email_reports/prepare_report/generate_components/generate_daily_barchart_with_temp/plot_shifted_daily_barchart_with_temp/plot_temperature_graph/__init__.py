
import matplotlib.ticker as ticker


def plot_temperature_graph(ax, sr_temp, fontsize=None, tick_range=None, label=None):

    if label is None:
        label = 'Temperature'

    if fontsize is None:
        fontsize = 13 

    # todo: month information can be removed df_occupancy

    # df_occupancy_cur.reset_index(drop=True, inplace=True)

    # the right y axis
    ax_r = ax.twinx() # instantiate a second axes that shares the same x-axis
    ax_r.yaxis.tick_left()
    ax_r.yaxis.set_label_position("left")
    ax_r.tick_params(axis='y', left=True, length=2, labelsize=fontsize)
    ax_r.set_ylabel(u'\N{DEGREE SIGN}'+'C', labelpad=5, fontsize=fontsize)
    ax_r.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))
    
    if tick_range is None:
        tick_value_o_max = sr_temp.max()
        tick_value_o_min = sr_temp.min()
        tick_value_o_var = tick_value_o_max - tick_value_o_min
        tick_range = [tick_value_o_min - tick_value_o_var*0.5, tick_value_o_max + tick_value_o_var*0.5]

    ax_r.set_ylim(tick_range)
    ax_r.plot(sr_temp, color= 'k', lw=0.1, ls='dashed', marker=".", ms=6, mec="k", label=label)
    ax_r.legend(loc='upper right', bbox_to_anchor=(0.92, 0.99), fontsize=fontsize, ncol=2)

    