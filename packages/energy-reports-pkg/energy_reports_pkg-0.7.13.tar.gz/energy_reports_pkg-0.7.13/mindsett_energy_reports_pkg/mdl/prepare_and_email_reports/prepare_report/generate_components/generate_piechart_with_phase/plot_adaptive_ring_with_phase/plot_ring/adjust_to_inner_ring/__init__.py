
import matplotlib.pyplot as plt

def adjust_to_inner_ring(ax, patch_for_gap, inner_radius, outer_radius, 
                         as_inner_ring=None):

    if as_inner_ring is None:
        as_inner_ring = False
    
    if as_inner_ring:

        # remove the inner line
        patch_for_gap.set(
                edgecolor=None,
                facecolor='w',
                hatch=None,
                radius=inner_radius+0.01, # added 0.01 to completely remove/cover the black line
                gid='no legend',
                )
        # p = plt.gcf()
        # p.gca().add_artist(patch_for_gap)
        ax.add_artist(patch_for_gap)

        # add the outer line
        outer_circle = plt.Circle((0, 0), outer_radius, 
                                    fill=False, 
                                    linewidth=1, 
                                    gid='no legend',
                                    edgecolor='k') # edgecolor=other_colours[0], 
        # p = plt.gcf()
        # p.gca().add_artist(outer_circle)
        ax.add_artist(outer_circle)