

def plot_the_legend(ax, 
                    fontsize=None,
                    bbox_to_anchor=None):

    if fontsize is None:
        fontsize = 13

    if bbox_to_anchor is None:
        bbox_to_anchor=(0.5, 0.99)

    # plot the legend
    ax.legend()
    legends = ax.get_legend()
    orig_handles = legends.legend_handles[:2]
    # for handle in orig_handles:
    #     print(f"{handle.set(ec='k') = }")

    # adj_handles = [handle.set(ec='k') for handle in orig_handles]
    _ = ax.legend(handles=orig_handles,
                 labels=['Total', 'In Hours'], 
                 loc='upper center', 
                 bbox_to_anchor=bbox_to_anchor, 
                 fontsize=fontsize, 
                 ncol=2)