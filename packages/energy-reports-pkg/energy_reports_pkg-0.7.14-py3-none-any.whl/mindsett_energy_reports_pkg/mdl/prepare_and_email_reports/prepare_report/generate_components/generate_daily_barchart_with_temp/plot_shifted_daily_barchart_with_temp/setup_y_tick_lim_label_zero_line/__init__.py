
import matplotlib.ticker as ticker

def setup_y_tick_lim_label_zero_line(ax, ls_ylim, display_unit, formatter,
                                     fontsize=None):

    if fontsize is None:
        fontsize = 13

    # move the y_tick to the right
    ax.yaxis.tick_right()
    ax.yaxis.set_label_position("right")
    ax.tick_params(axis='y', right=True, length=5, pad=9, labelsize=fontsize)
    ax.set_ylim(ls_ylim)

    # set y label
    ax.set_ylabel(f"Daily Usage ({display_unit})", labelpad=18, fontsize=fontsize)

    # set yaxis formatter
    ax.yaxis.set_major_formatter(ticker.FormatStrFormatter(formatter))

    # plot the zero value horizontal line
    ax.axhline(y=0, color='k', linestyle=':', zorder=-1)