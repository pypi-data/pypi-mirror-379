

def adjust_gap_for_visibility(gap_value, non_gap_value, 
                              min_vis_pct=None):
    
    if min_vis_pct is None:
        min_vis_pct = 3

    min_non_gap_pct = min_vis_pct
    max_non_gap_pct = 100 - min_non_gap_pct

    max_gap_for_visibility = (100 - min_non_gap_pct)*non_gap_value/min_non_gap_pct
    min_gap_for_visibility = (100 - max_non_gap_pct)*non_gap_value/max_non_gap_pct

    adj_gap_for_visibility = gap_value
    adj_gap_for_visibility = min(max_gap_for_visibility, adj_gap_for_visibility)
    adj_gap_for_visibility = max(min_gap_for_visibility, adj_gap_for_visibility)

    return adj_gap_for_visibility