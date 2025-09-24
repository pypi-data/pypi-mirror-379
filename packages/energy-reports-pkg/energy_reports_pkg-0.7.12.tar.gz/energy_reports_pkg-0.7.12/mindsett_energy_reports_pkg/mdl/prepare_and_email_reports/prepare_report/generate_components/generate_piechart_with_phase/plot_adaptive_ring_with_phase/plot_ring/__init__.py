
import matplotlib.pyplot as plt
import copy

from .adjust_gap_for_visibility import adjust_gap_for_visibility
from .adjust_to_inner_ring import adjust_to_inner_ring
from .annotate_pct_on_pies import annotate_pct_on_pies
from .generate_pct_fmt import generate_pct_fmt
from .adjust_values_for_better_visibility import adjust_values_for_better_visibility


def plot_ring(sr_orig, ax,
                colors=None,
                hatch=None,
                fontsize=None,
                as_inner_ring=None,
                inner_radius=None,
                outer_radius=None,
                gap_value=None, 
                ann_pct=None,
                pct_out=None, 
                pct_hide=None):
    
    if fontsize is None:
        fontsize = 13
    if colors is None:
        colors = ['#fffffc'] # use this modification of white color to differentiate it from the actual white, for legend handle filter
    if as_inner_ring is None:
        as_inner_ring = False
    if inner_radius is None:
        inner_radius = 0.5
    if outer_radius is None:
        outer_radius = 1
    if ann_pct is None:
        ann_pct = True
    if gap_value is None:
        gap_value = 0
    
    sr = adjust_values_for_better_visibility(sr_orig) # to avoid changes made to the original series

    ls_orig_pct_fmt = generate_pct_fmt(sr)
    
    if gap_value > 0:

        sr_sum_without_gap = sr.sum()

        # to make the non-gap pie or gap pie more visible
        sr['Gap Value'] = adjust_gap_for_visibility(gap_value, sr_sum_without_gap, 
                                                    min_vis_pct=3)
        
    sr.plot.pie(ax=ax, 
                autopct='', # needed to generate placeholder for ax.texts
                colors=colors,
                hatch=hatch,
                radius=outer_radius,
                # frame=True,
                textprops={"color": 'k', 
                            "fontsize": fontsize}, 
                pctdistance=0.77,
                wedgeprops={'linewidth': 1, 
                            "edgecolor": 'k'}, 
                startangle=90,
                labels=None)
    
    if gap_value > 0:
        patch_for_gap = copy.copy(ax.patches[-1])
        ax.patches[-1].set(visible=False, gid='no legend')

    if ann_pct:
        annotate_pct_on_pies(ax, sr, ls_orig_pct_fmt, 
                            pct_hide=pct_hide,
                            pct_out=pct_out)
    
    # plot the circle in the centre of the ring
    inner_circle = plt.Circle((0, 0), inner_radius, 
                              facecolor='w', 
                              linewidth=1, 
                              edgecolor='k') # edgecolor=other_colours[0], 
    # p = plt.gcf()
    # p.gca().add_artist(inner_circle)
    ax.add_artist(inner_circle)

    if gap_value > 0:
        adjust_to_inner_ring(ax, patch_for_gap, inner_radius, outer_radius, 
                        as_inner_ring=as_inner_ring)

    ax.set_ylabel("")
