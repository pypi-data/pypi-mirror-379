
import matplotlib.pyplot as plt

from .plot_ring import plot_ring
from .plot_centre_pct import plot_centre_pct
from .show_legend import show_legend
from .plot_phase_balance import plot_phase_balance

# cd = {"tomato": '#FF836A',
#       "aquablue": '#6DC2B3',
#       "peach": '#FED6D2',
#       "darkgrey": '#9F9D9C',
#       "potato": '#FEF8C8',
#       "cyan": '#B6E4E1',
#       "dimgray":'#696969',
#       "Seafoam":'#87e0cf',
#       "gainsboro":'#DCDCDC',
#       "grey": '#808080',
#       "brown": '#964B00',
#       "black": '#000000'}

def plot_adaptive_ring_with_phase(df_pre_pie,
                                    phase_values_list,
                                    colors=None,
                                    hatches=None,
                                    sum_column = None, 
                                    pct_column = None,
                                    gene_column = None,
                                    fontsize=None,
                                    ):
    
    if colors is None:
        from .colors import colors

    if hatches is None:
        from .hatches import hatches
    
    if sum_column is None:
        sum_column = "sum_abs"

    if gene_column is None:
        gene_column = 'generator'

    fig, ax = plt.subplots(1, 1, figsize=(9, 3.5))

    # gs = fig.add_gridspec(2, hspace=0)
    # axs = gs.subplots(sharex=True, sharey=True)

    if df_pre_pie[gene_column].nunique() == 2:

        sr_outer = df_pre_pie.loc[df_pre_pie[gene_column]==False, sum_column]
        sr_inner = df_pre_pie.loc[df_pre_pie[gene_column]==True, sum_column]
        gap_value = sr_inner.sum() - sr_outer.sum()
        outer_ring_inner_radius = 0.55
        asset_total = sr_inner.sum() + sr_outer.sum()
    else:
        sr_outer = df_pre_pie[sum_column]
        gap_value = None
        outer_ring_inner_radius = 0.50
        asset_total = sr_outer.sum()
    
    print('consumption_mwh_subchannel_sum: ', asset_total/1000) # debug

    # plot the outer ring
    plot_ring(sr_outer, ax,
                    colors=colors, 
                    fontsize=fontsize, 
                    gap_value=gap_value, 
                    outer_radius=1, 
                    inner_radius=outer_ring_inner_radius,
                    ann_pct=True, 
                    as_inner_ring=False)

    # plot the inner ring and pct text in the middle conditionally
    if df_pre_pie[gene_column].nunique() == 2:
        plot_ring(sr_inner, ax, 
                        hatch=hatches, 
                        fontsize=fontsize, 
                        gap_value=-gap_value, 
                        outer_radius=0.5, 
                        inner_radius=0.3,
                        ann_pct=False, 
                        as_inner_ring=True)

        assets_source_pct = sr_inner.sum()/sr_outer.sum()
        plot_centre_pct(ax, assets_source_pct, 
                        fontsize=fontsize)

    show_legend(ax, df_pre_pie, 
                fontsize=fontsize,
                sum_column=sum_column, 
                pct_column=pct_column)

    # ruler settings
    ru_x = 0.01  # the x-axis of phase balance ruler
    ru_y = 0  # the x-axis of phase balance ruler
    ru_w = 2  # the width of phase balance ruler
    ru_h = 0.06 # the height of phase balance ruler

    plot_phase_balance(ax, phase_values_list,
                        fontsize=fontsize,
                        ru_x=ru_x,
                        ru_y=ru_y,
                        ru_h=ru_h,
                        ru_w=ru_w)

    fig.tight_layout(pad=0, rect=[-0.2, -0.0, 0.608, 0.99])

    ax.set_ylim(-1.75, 1.6)
