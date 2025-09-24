

def get_legend_handles(ax, no_of_labels=50):

    ax.legend(labels=['']*no_of_labels)

    legends = ax.get_legend()

    valid_handles = []

    for handle in legends.legend_handles:

        is_invisible_pie_for_gap = (handle.get_visible()==False)
        is_white_pie_in_ring_centre = (handle.get_fc() == (1.0, 1.0, 1.0, 1))
        is_outer_gap_edge_when_as_inner = (handle.get_fc()[3]==0)

        invalid_handle = (is_invisible_pie_for_gap or is_white_pie_in_ring_centre or is_outer_gap_edge_when_as_inner)

        if not invalid_handle: 
            valid_handles.append(handle)

    return valid_handles