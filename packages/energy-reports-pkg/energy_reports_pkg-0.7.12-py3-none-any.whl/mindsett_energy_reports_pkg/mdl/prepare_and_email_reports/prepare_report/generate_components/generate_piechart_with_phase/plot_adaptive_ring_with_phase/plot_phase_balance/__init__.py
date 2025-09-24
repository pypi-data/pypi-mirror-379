
# import matplotlib.patches as mpatches

from .plot_phase_balance_part import plot_phase_balance_part
from .get_tick_values import get_tick_values
from .get_phase_markers import get_phase_markers

color_dict = {"grey":  '#808080',
              "brown": '#964B00',
              "black": '#000000'}

def plot_phase_balance(ax, phase_values_list,
                    fontsize=None,
                    ru_x=None,
                    ru_y=None,
                    ru_h=None,
                    ru_w=None):
    
    phase_markers_list = get_phase_markers(phase_values_list)

    part_control_ls = [{'ruler_part_color': color_dict["brown"],
                        'phase_marker': phase_markers_list[0],
                         'part': 'part_one',
                         'part_idx': 1},
                        {'ruler_part_color': color_dict["black"],
                        'phase_marker': phase_markers_list[1],
                         'part': 'part_two',
                         'part_idx': 2},
                        {'ruler_part_color': color_dict["grey"],
                        'phase_marker': phase_markers_list[2],
                         'part': 'part_three',
                         'part_idx': 3}]
    
    ticks_values_list = get_tick_values(phase_values_list)

    for part_control in part_control_ls:
        plot_phase_balance_part(ax, ticks_values_list, part_control,
                                fontsize=fontsize,
                                ru_x=ru_x,
                                ru_y=ru_y,
                                ru_h=ru_h,
                                ru_w=ru_w)
