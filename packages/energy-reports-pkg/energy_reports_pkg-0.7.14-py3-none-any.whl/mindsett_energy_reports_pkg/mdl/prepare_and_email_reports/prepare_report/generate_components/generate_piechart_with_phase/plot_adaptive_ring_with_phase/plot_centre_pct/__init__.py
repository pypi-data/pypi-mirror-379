
import matplotlib.pyplot as plt



def plot_centre_pct(ax, assets_source_pct, 
                    fontsize=None):

    if fontsize is None:
        fontsize = 13
    
    assets_source_pct_value = assets_source_pct*100 

    # print(f'{assets_source_pct_value = }')
    # ensure the digits are readable
    if assets_source_pct_value >= 1:
        assets_source_pct_fmt = f'{assets_source_pct_value:.0f}%'
    elif assets_source_pct_value >= 0.1:
        assets_source_pct_fmt = f'{assets_source_pct_value:.1f}%'
    elif assets_source_pct_value >= 0.01:
        assets_source_pct_fmt = f'{(assets_source_pct_value*10):.1f}‰'
    else:
        assets_source_pct_fmt = f'<0.1‰'

    ax.text(0, 0, assets_source_pct_fmt, 
            fontsize=fontsize,
            horizontalalignment='center',
            verticalalignment='center')