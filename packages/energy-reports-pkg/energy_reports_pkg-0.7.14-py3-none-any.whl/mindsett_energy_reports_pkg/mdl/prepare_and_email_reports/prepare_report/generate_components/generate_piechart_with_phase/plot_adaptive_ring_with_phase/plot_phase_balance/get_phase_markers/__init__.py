

def get_phase_markers(phase_values_list, 
                      var_allowance_pct=None):

    balanced_avg_value = sum(phase_values_list)/3

    if var_allowance_pct is None:
        var_allowance_pct = 0.04

    var_allowance_value = balanced_avg_value * var_allowance_pct

    markers_list = []
    for phase_value in phase_values_list:

        if phase_value > (balanced_avg_value + var_allowance_value):
            marker_text = '>'
        elif phase_value > (balanced_avg_value - var_allowance_value):
            marker_text = '='
        elif phase_value > 0:
            marker_text = '<'
        else:
            marker_text = '?'

        markers_list.append(marker_text)
    
    return markers_list
        