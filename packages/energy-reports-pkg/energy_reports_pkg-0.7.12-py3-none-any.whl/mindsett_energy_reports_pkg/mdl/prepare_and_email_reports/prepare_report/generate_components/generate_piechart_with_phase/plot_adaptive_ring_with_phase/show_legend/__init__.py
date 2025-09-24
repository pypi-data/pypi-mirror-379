

from .get_legend_handles import get_legend_handles
from .generate_legend_labels import generate_legend_labels

def show_legend(ax, df_pre_pie, 
                fontsize=None,
                sum_column=None, 
                pct_column=None):
    
    if fontsize is None:
        fontsize = 13

    valid_handles = get_legend_handles(ax)
    legend_labels = generate_legend_labels(df_pre_pie, 
                                            sum_column=sum_column, 
                                            pct_column=pct_column)

    x0, y0, width, height = 1.15, 0.5, 0, 0 
    leg_ncol = 1
    leg_loc = 'center left'

    leg = ax.legend(handles=valid_handles,
                    labels=legend_labels,
                    loc=leg_loc,
                    facecolor='w', 
                    edgecolor='w',
                    borderaxespad=0,
                    bbox_to_anchor=(x0, y0, width, height), 
                    fontsize=fontsize,  
                    ncol=leg_ncol, 
                    handleheight=1.2, 
                    labelspacing=0.6, 
                    title=None)

    leg.set_in_layout(False)