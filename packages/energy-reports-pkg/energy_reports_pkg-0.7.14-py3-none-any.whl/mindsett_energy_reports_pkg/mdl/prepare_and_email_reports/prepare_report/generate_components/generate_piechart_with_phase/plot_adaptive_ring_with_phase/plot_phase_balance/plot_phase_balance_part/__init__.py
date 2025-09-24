
import matplotlib.patches as mpatches

from .ruler_anno_shink_cf import ruler_anno_shink_cf

def plot_phase_balance_part(ax, ticks_values_list, part_control,
                         fontsize=None,
                         fx=None,
                         fy=None,
                         fs=None,
                         ru_x=None,
                         ru_y=None,
                         ru_h=None,
                         ru_w=None):

    if fontsize is None:
        fontsize = 13

    # fancy box setting
    if fx is None:
        fx = -1  # fancy box x-axis value
    if fy is None:
        fy = -1.3  # fancy box y-axis value
    if fs is None:
        fs = 1  # fancy box scale factor

    # ruler settings
    if ru_x is None:
        ru_x = 0  # the x-axis of benchmarking ruler
    if ru_y is None:
        ru_y = 0  # the x-axis of benchmarking ruler
    if ru_h is None:
        ru_h = 0.03  # the height of benchmarking ruler
    if ru_w is None:
        ru_w = 1  # the width of benchmarking ruler

    ruler_part_color = part_control['ruler_part_color']
    part = part_control['part']
    part_idx = part_control['part_idx']
    phase_marker = part_control['phase_marker']
    # text_color = part_control['text_color']

    # ticks range
    ticks_max = max(ticks_values_list)
    ticks_min = min(ticks_values_list)
    ticks_range = ticks_max - ticks_min
    
    # rp_edgecolor = 'k' # edgecolor of the ruler body parts
    rp_note_fontsize = fontsize - 5 # the fontsize of notes on ruler parts # please note that the other sizes except default 13 haven't been tested yet

    # ruler body - rectangle bar
    rp_x = ru_x + ru_w * (ticks_values_list[part_idx-1]-ticks_min)/ticks_range       # the x-axis value of this part
    rp_y = ru_y - 0.03 # - 0.1 # 0.14      # the y-axis value of this part
    rp_pct = (ticks_values_list[part_idx]-ticks_values_list[part_idx-1])/ticks_range
    rp_w = ru_w * rp_pct   # the width value of this part
    rp_h = ru_h
    rp_c = ruler_part_color
    ruler_body_part = mpatches.Rectangle([fx+rp_x*fs, fy+rp_y*fs], rp_w*fs, rp_h*fs, 
                                         facecolor=rp_c, 
                                         edgecolor='w', 
                                         lw=2)
    ax.add_artist(ruler_body_part)

    # ruler body - annotation on the bar
    rpa_x = rp_x + rp_w/2.0 # ruler body part annotation - x axis
    rpa_y = rp_y + 0.076 # ruler body part annotation - y axis
    bar_width = rp_w*fs
    # part = 'part_one'
    rpa_text = ruler_anno_shink_cf(bar_width, part)
    
    ax.annotate(rpa_text, (fx+fs*rpa_x, fy+fs*rpa_y), 
                color= 'w', # '#B87333', # text_color, 
                weight='extra bold', 
                fontsize=rp_note_fontsize, 
                ha='center', 
                va='center')
    
    # ruler body - marker symbol below the bar
    rps_x = rp_x + rp_w/2.0 # ruler body part annotation - x axis
    sym_pad_y = (-0.18)
    rps_y = rp_y + sym_pad_y  # ruler body part annotation - y axis
    bar_width = rp_w*fs
    rp_maker_fontsize = fontsize +2 # make it bigger than the annotation text, to be more visible

    # print(f'{rp_pct = }')

    # balance_value = 1./3
    # variance_allowance = 0.04/3

    # if rp_pct > (balance_value + variance_allowance):
    #     rps_text = '>'
    # elif rp_pct > (balance_value - variance_allowance):
    #     rps_text = '='
    # elif rp_pct > 0:
    #     rps_text = '<'
    # else:
    #     rps_text = '?'

    # rpa_text = ruler_anno_shink_cf(bar_width, part)
    symbol_color = 'k'
    
    ax.annotate(phase_marker, (fx+fs*rps_x, fy+fs*rps_y), 
                color=symbol_color, 
                weight='extra bold', 
                fontsize=rp_maker_fontsize, 
                ha='center', 
                va='center')
    