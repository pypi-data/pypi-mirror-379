
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

import matplotlib.image as mpimg
import matplotlib.patches as mpatches
import matplotlib.text as mpltext

from os import path

cd = {"tomato": '#FF836A',"aquablue": '#6DC2B3',"peach": '#FED6D2',"darkgrey": '#9F9D9C',"potato": '#FEF8C8',
      "cyan": '#B6E4E1',"dimgray":'#696969',"Seafoam":'#87e0cf',"gainsboro":'#DCDCDC'}

def energy_meter_design(ax, consumption_mwh_cur, consumption_mwh_pre, image_folder,
                        conv_mwh_co2 = 0.233,
                        conv_mwh_price = 190,
                        fx = 0.2, # fancy box x-axis value
                        fy = 0.3, # fancy box y-axis value
                        fs  = 0.6, # fancy box scale factor
                        currency = 'GBP',
                        fontsize = 13
                        ):

    ax.set_xlim(0.2, 0.9)
    ax.set_ylim(0.2, 0.9)
    iz  = 0.06 * fs # icon zooming factor

    # add a fancy box as the energy meter outline

    fancybox_width  = fs
    fancybox_height = fs
    fancybox = mpatches.FancyBboxPatch(
                [fx, fy], fancybox_width, fancybox_height, fc="w", ec='k', lw=1.5, ls= 'dotted',
                boxstyle=mpatches.BoxStyle("Round", rounding_size=0.07, pad=0.02))
    ax.add_artist(fancybox)

    notes_fontsize = fontsize - 2
    # text sub-title 
    text_title = mpltext.Text(x=fx+0.45*fs, y=fy+0.7*fs, text=f'Equivalent$^*$', 
                              va=u'baseline', color='grey', ha=u'right', fontweight='light',fontstyle='italic', fontsize=notes_fontsize)
    ax.add_artist(text_title)

    # text footnote

    ## currency_symbol selection
    currency_symbol_dict = {
        'GBP': '£',
        'EUR': '€',
        'USD': '\$',
        'SGD': 'S\$'
    }
    try: 
        currency_symbol = currency_symbol_dict[currency]
    except:
        raise Exception('There is no symbol provided for this currency!')

    ## symbol selection
    text_footnote_with_co2 = f'* {conv_mwh_co2:1.3f}$t$ CO2e $\Leftrightarrow$ 1MWh $\Leftrightarrow$ {currency_symbol}{conv_mwh_price:1.1f}' # not used for now - 2024 Sep 23th
    text_footnote_without_co2 = f'* 1MWh $\Leftrightarrow$ {currency_symbol}{conv_mwh_price:1.1f}'
    text_footnote = mpltext.Text(x=fx+0.5*fs, y=fy+0.04*fs, text=text_footnote_without_co2, 
                                 va=u'baseline', color='k', ha=u'center', fontsize=notes_fontsize)
    ax.add_artist(text_footnote)

    ## text readings settings
    re_w = 0.80   # reading width
    re_x = 0.127  # reading x-axis value
    re_y = 0.80   # reading y-axis value
    re_c = "k"    # reading colour
    r_fs = fontsize + 3   # reading fontsize # please note that the other sizes except default 13 haven't been tested yet
    mr_fs = fontsize + 5    # main reading fontsize # please note that the other sizes except default 13 haven't been tested yet

    ## reading - energy 
    reading = consumption_mwh_cur

    reading_abs = abs(reading) # the default unit is MWh

    # adjust the decimal point and the unit based on the actual value
    if reading_abs > 10:
        reading_value = f"{reading:.0f} MWh"
    elif reading_abs > 1:
        reading_value = f"{reading:.1f} MWh"
    elif reading_abs*1000 > 10:
        reading_value = f"{reading*1000:.0f} KWh"
    elif reading_abs*1000 > 1:
        reading_value = f"{reading*1000:.1f} KWh"
    elif reading_abs*1000_000 > 10:
        reading_value = f"{reading*1000_000:.0f} Wh"
    else:
        reading_value = f"{reading*1000_000:.1f} Wh"
    # reading - energy - text - monthly total
    rt_x = re_x + 0.15 + 0.03
    rt_y = re_y
    readingtext = mpltext.Text(x=fx+rt_x*fs, y=fy+rt_y*fs, text=f'{reading_value}', 
                               va=u'bottom', color=re_c, ha=u'center', fontweight="bold", fontsize=mr_fs)

    # reading - energy - text - monthly change
    rt_x = re_x + 0.65
    rt_y = re_y + 0.02


    change_value = (consumption_mwh_cur - consumption_mwh_pre) / abs(consumption_mwh_pre)
    change_value_int = int(change_value*100)

    # print(f'{consumption_mwh_cur = }')
    # print(f'{consumption_mwh_pre = }')
    # print(f'{change_value = }')


    if change_value_int > 0: 
        change_arrow_str = r'${\blacktriangle}$'
    elif change_value_int < 0:
        change_arrow_str = r'$\:\!\triangledown\:\!$'
    else :
        change_arrow_str = r'--'


    change_in_percentage_value = int(abs(change_value)*100)

    if change_in_percentage_value > 999:
        change_in_percentage_value_str = r"$\,$" + ">999" + "%"
    elif change_in_percentage_value > 99: 
        change_in_percentage_value_str = r"$\,$" + str(change_in_percentage_value) + "%"
    elif change_in_percentage_value > 9: 
        change_in_percentage_value_str = " " + str(change_in_percentage_value) + r"$\,$" + "%"
    else:
        change_in_percentage_value_str = " " + str(change_in_percentage_value) + r"$\;$" + "%"


    change_in_percentage = change_arrow_str + change_in_percentage_value_str
    text_percentage = mpltext.Text(x=fx+rt_x*fs, y=fy+rt_y*fs, text=f'{change_in_percentage}', 
                                   va=u'baseline', color='k', ha=u'center', fontweight="bold", fontsize=mr_fs)
    ax.add_artist(text_percentage)

    # horizontal line to separate the different readings
    rl_x = re_x * 0.2       # the x-axis value of the line at the bottom of the reading 
    rl_y = re_y - 0.15        # the y-axis value of the line at the bottom of the reading
    rl_w = re_w * 1.2    # the width value of the line at the bottom of the reading
    horizontal_line = mpatches.Rectangle([fx+rl_x*fs, fy+rl_y*fs], 
                                         rl_w*fs, 0, facecolor="k", edgecolor='k', lw=1, ls= 'dotted')
    ax.add_artist(readingtext)
    ax.add_artist(horizontal_line)


    ## reading - co2
    re_y = 0.48
    reading = consumption_mwh_cur * conv_mwh_co2

    # adjust the unit based on value
    reading_value = f"{reading:1.1f} tons"
    if reading_value == '0.0 tons':
        reading_value = f"{round(reading*1000)} kg"
        
    image_name = 'co2.png'

    # reading - co2 - icon
    ri_x = re_x + 0.09  # reading icon x-axis value
    ri_y = re_y + 0.042
    icon = mpimg.imread(image_folder + image_name)
    ibox = OffsetImage(icon, zoom=2*iz)
    readingicon = AnnotationBbox(ibox, (fx+ri_x*fs, fy+ri_y*fs), frameon = False)

    # reading - co2 - text
    rt_x = re_x + 0.342
    rt_y = re_y
    readingtext = mpltext.Text(x=fx+rt_x*fs, y=fy+rt_y*fs, text=f'{reading_value}', 
                               va=u'bottom', color=re_c, ha=u'left', fontweight="bold", fontsize=r_fs)

    # horizontal line to separate the different readings
    rl_x = re_x         # the x-axis value of the line at the bottom of the reading 
    rl_y = re_y - 0.07      # the y-axis value of the line at the bottom of the reading
    rl_w = re_w * 0.9   # the width value of the line at the bottom of the reading
    horizontal_line = mpatches.Rectangle([fx+rl_x*fs, fy+rl_y*fs], 
                                         rl_w*fs, 0, facecolor="k", edgecolor='k', lw=1, ls= 'dotted')

    ax.add_artist(readingicon)
    ax.add_artist(readingtext)
    ax.add_artist(horizontal_line)


    ## reading - billing
    re_y = 0.23
    reading = consumption_mwh_cur * conv_mwh_price
    reading_value = f"{reading:,.2f}".replace(".", ". ") 

    # adjust the size for visual effect
    if len(reading_value) > 8:
        reading_value = reading_value.replace(". ", ".") 
        if len(reading_value) > 8:
            reading_value = reading_value[:-2]

    # reading - billing - icon

    ## icon selection
    currency_icon_dict = { # please note that the format has to be 512px png
        'GBP': 'pound-sterling.png',
        'EUR': 'euros.png',
        'USD': 'dollar-symbol.png', # https://www.flaticon.com/free-icon/dollar-symbol_1140418?term=dollar+symbol&page=1&position=22&origin=search&related_id=1140418
        'SGD': 'singapore-dollar.png' # https://www.flaticon.com/free-icon/singapore-dollar_9921422?term=singapore+dollar&page=3&position=73&origin=search&related_id=9921422
    }
    try: 
        image_name = currency_icon_dict[currency]
    except:
        raise Exception('There is no icon provided for this currency!')

    ## icon plotting
    ri_x = re_x + 0.09  # reading icon x-axis value
    ri_y = re_y + 0.06
    icon = mpimg.imread(image_folder + image_name)
    ibox = OffsetImage(icon, zoom=1.6*iz)
    readingicon = AnnotationBbox(ibox, (fx+ri_x*fs, fy+ri_y*fs), frameon = False)

    # reading - billing - text
    rt_x = re_x + 0.342
    rt_y = re_y
    readingtext = mpltext.Text(x=fx+rt_x*fs, y=fy+rt_y*fs, text=f'{reading_value}', 
                               va=u'bottom', color=re_c, ha=u'left', fontweight="bold", fontsize=r_fs)

    # horizontal line to separate the different readings
    rl_x = re_x          # the x-axis value of the line at the bottom of the reading 
    rl_y = re_y - 0.07        # the y-axis value of the line at the bottom of the reading
    rl_w = re_w * 0.9    # the width value of the line at the bottom of the reading
    horizontal_line = mpatches.Rectangle([fx+rl_x*fs, fy+rl_y*fs], 
                                         rl_w*fs, 0, facecolor="k", edgecolor='k', lw=1, ls= 'dotted')

    ax.add_artist(readingicon)
    ax.add_artist(readingtext)
    ax.add_artist(horizontal_line)


    ## benchmarking design
    re_y = 0.65
    ri_y = re_y + 0.07*fs

    ax.axis('equal')