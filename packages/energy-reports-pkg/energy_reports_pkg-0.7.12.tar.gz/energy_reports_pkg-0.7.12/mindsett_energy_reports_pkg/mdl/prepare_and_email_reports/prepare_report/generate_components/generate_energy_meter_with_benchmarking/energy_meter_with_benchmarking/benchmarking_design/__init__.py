
import matplotlib.patches as mpatches
import matplotlib.text as mpltext

from .ruler_anno_shink_cf import ruler_anno_shink_cf


cd = {"tomato": '#FF836A',"aquablue": '#6DC2B3',"peach": '#FED6D2',"darkgrey": '#9F9D9C',"potato": '#FEF8C8',
      "cyan": '#B6E4E1',"dimgray":'#696969',"Seafoam":'#87e0cf',"gainsboro":'#DCDCDC'}


def benchmarking_design(ax, consumption_mwh_cur, floor_sqm,
                        kwh_per_sqm_good = 10.33,
                        kwh_per_sqm_typical = 14.5,
                        fx = 0.2, # fancy box x-axis value
                        fy = 0.18, # fancy box y-axis value
                        fs = 0.6, # fancy box scale factor
                        fontsize = 13
                        ):


        mwh_good = floor_sqm * kwh_per_sqm_good / 1000
        mwh_typical = floor_sqm * kwh_per_sqm_typical / 1000
        
        mwh_btw_good_typical = mwh_typical - mwh_good
        
        key_values_list = [mwh_typical + mwh_btw_good_typical,
                           mwh_good - mwh_btw_good_typical,
                           consumption_mwh_cur + mwh_btw_good_typical/2,
                           consumption_mwh_cur - mwh_btw_good_typical/2]
        
        ticks_max = max(key_values_list)
        ticks_min = min(key_values_list)
        
        ticks_values_list = [ticks_min, mwh_good, mwh_typical, ticks_max]
        ticks_range = ticks_max - ticks_min
        
        ## ruler settings
        ru_x = 0  # the x-axis of benchmarking ruler
        ru_y = 0  # the x-axis of benchmarking ruler
        ru_w = 1  # the width of benchmarking ruler
        ru_h = 0.08  # the height of benchmarking ruler
        
        rp_edgecolor = 'k' # edgecolor of the ruler body parts
        rp_note_fontsize = fontsize - 5 # the fontsize of notes on ruler parts # please note that the other sizes except default 13 haven't been tested yet

        # ruler body - part one - good
        rp_x = ru_x         # the x-axis value of this part
        rp_y = ru_y - 0.07      # the y-axis value of this part
        rp_w = ru_w * (ticks_values_list[1]-ticks_values_list[0])/ticks_range   # the width value of this part
        rp_h = ru_h
        rp_c = cd["aquablue"]
        ruler_body_part_one = mpatches.Rectangle([fx+rp_x*fs, fy+rp_y*fs], 
                                             rp_w*fs, rp_h*fs, facecolor=rp_c, edgecolor=rp_edgecolor, lw=1)
        
      #   print('ruler_body_part_one rp_w*fs, rp_h*fs: ', rp_w*fs, rp_h*fs)
        rpa_x = rp_x + rp_w/2.0 # ruler body part annotation - x axis
        rpa_y = rp_y  # ruler body part annotation - y axis
        bar_width = rp_w*fs
        part = 'part_one'
        rpa_text = ruler_anno_shink_cf(bar_width, part)
        

        ax.annotate(rpa_text, (fx+fs*rpa_x, fx+fs*rpa_y), color='w', weight='bold', 
                    fontsize=rp_note_fontsize, ha='center', va='center')

        # ruler body - part two - normal
        rp_x = rp_x + rp_w     # the x-axis value of this part
        rp_y = ru_y - 0.07      # the y-axis value of this part
        rp_w = ru_w * (ticks_values_list[2]-ticks_values_list[1])/ticks_range   # the width value of this part
        rp_h = ru_h
        rp_c = cd["potato"]
        ruler_body_part_two = mpatches.Rectangle([fx+rp_x*fs, fy+rp_y*fs], 
                                             rp_w*fs, rp_h*fs, facecolor=rp_c, edgecolor=rp_edgecolor, lw=1)
        
      #   print('ruler_body_part_two rp_w*fs, rp_h*fs: ', rp_w*fs, rp_h*fs)
        rpa_x = rp_x + rp_w/2.0 # ruler body part annotation - x axis
        rpa_y = rp_y  # ruler body part annotation - y axis
        bar_width = rp_w*fs
        part = 'part_two'
        rpa_text = ruler_anno_shink_cf(bar_width, part)

        ax.annotate(rpa_text, (fx+fs*rpa_x, fx+fs*rpa_y), color='#9F9D9C', weight='bold', 
                    fontsize=rp_note_fontsize, ha='center', va='center')

        # ruler body - part three - poor
        rp_x = rp_x + rp_w     # the x-axis value of this part
        rp_y = ru_y - 0.07      # the y-axis value of this part
        rp_w = ru_w * (ticks_values_list[3]-ticks_values_list[2])/ticks_range   # the width value of this part
        rp_h = ru_h
        rp_c = cd["tomato"]
        ruler_body_part_thr = mpatches.Rectangle([fx+rp_x*fs, fy+rp_y*fs], 
                                             rp_w*fs, rp_h*fs, facecolor=rp_c, edgecolor=rp_edgecolor, lw=1)
        
      #   print('ruler_body_part_three rp_w*fs, rp_h*fs: ', rp_w*fs, rp_h*fs)
        rpa_x = rp_x + rp_w/2.0 # ruler body part annotation - x axis
        rpa_y = rp_y  # ruler body part annotation - y axis
        bar_width = rp_w*fs
        part = 'part_three'
        rpa_text = ruler_anno_shink_cf(bar_width, part)

        ax.annotate(rpa_text, (fx+fs*rpa_x, fx+fs*rpa_y), color='w', weight='bold', 
                    fontsize=rp_note_fontsize, ha='center', va='center')

        ax.add_artist(ruler_body_part_one)
        ax.add_artist(ruler_body_part_two)
        ax.add_artist(ruler_body_part_thr)


        # ruler ticks labels
        
        rt_fs = fontsize  # the fontsize of ruler ticks labels
        rt_c = "grey"  # the font color of ruler ticks labels
        rt_va = u'bottom' 
        rt_ha = u'center' 
        rt_fontweight = "light"
        
        ru_rt_y = -0.18 # ruler ticks y-axis in relation to the ruler y-axis
        
        tick = ticks_values_list[0]
        rt_x = ru_x + (tick-ticks_min)/ticks_range
        rt_y = ru_y + ru_rt_y
        tick_value = f"{tick:1.1f}"
        tick_label_one = mpltext.Text(x=fx+rt_x*fs, y=fy+rt_y*fs, text=f'{tick_value}', 
                                  va=rt_va, color=rt_c, ha=rt_ha, fontweight=rt_fontweight, fontsize=rt_fs)

        tick = ticks_values_list[1]
        tick_pct = (tick-ticks_min)/ticks_range
        rt_x = ru_x + tick_pct
        rt_y = ru_y + ru_rt_y

        # conditionally remove the tick_value label when it's too close to the edges
        if (tick_pct < 0.2) or (tick_pct > 0.8):
            tick_value = ''
        else:
            tick_value = f"{tick:1.1f}"
        tick_label_two = mpltext.Text(x=fx+rt_x*fs, y=fy+rt_y*fs, text=f'{tick_value}', 
                                  va=rt_va, color=rt_c, ha=rt_ha, fontweight=rt_fontweight, fontsize=rt_fs)

        tick = ticks_values_list[2]
        tick_pct = (tick-ticks_min)/ticks_range
        rt_x = ru_x + tick_pct
        rt_y = ru_y + ru_rt_y

        # conditionally remove the tick_value label when it's too close to the edges
        if (tick_pct < 0.2) or (tick_pct > 0.8):
            tick_value = ''
        else:
            tick_value = f"{tick:1.1f}"
        tick_label_thr = mpltext.Text(x=fx+rt_x*fs, y=fy+rt_y*fs, text=f'{tick_value}', 
                                  va=rt_va, color=rt_c, ha=rt_ha, fontweight=rt_fontweight, fontsize=rt_fs)

        tick = ticks_values_list[3]
        rt_x = ru_x + (tick-ticks_min)/ticks_range
        rt_y = ru_y + ru_rt_y
        tick_value = f"{tick:1.1f}"
        tick_label_four = mpltext.Text(x=fx+rt_x*fs, y=fy+rt_y*fs, text=f'{tick_value}', 
                                  va=rt_va, color=rt_c, ha=rt_ha, fontweight=rt_fontweight, fontsize=rt_fs)

        ax.add_artist(tick_label_one)
        ax.add_artist(tick_label_two)
        ax.add_artist(tick_label_thr)
        ax.add_artist(tick_label_four)

        # ruler indicator
        indicator_value = consumption_mwh_cur
        rih_x = ru_x + (indicator_value-ticks_min)/ticks_range # x-axis value of the ruler indicator head
        rih_y = ru_y + 0.084  # y-axis value of the ruler indicator head
        rih_r = 0.045

        indicator_head = mpatches.Circle((fx+(rih_x)*fs, fy+rih_y*fs), rih_r*fs, 
                                         fc="w", color = "w", ec="k", lw=1.3, zorder=10
                                         ) #path_effects=[path_effects.withSimplePatchShadow()]

        rib_x = ru_x + (indicator_value-ticks_min)/ticks_range # x-axis value of the ruler indicator head
        rib_y = ru_y - 0.09  # y-axis value of the ruler indicator head
        rib_w = 0.02
        rib_h = ru_h * 2

        indicator_body = mpatches.Rectangle([fx+(rib_x-rib_w/2)*fs, fy+rib_y*fs], rib_w*fs, rib_h*fs, 
                                            fc="w", ec="k", lw=1.3,  zorder=10) #path_effects=[path_effects.withSimplePatchShadow()]
        ax.add_artist(indicator_body)
        ax.add_artist(indicator_head)
        
        ## title

        tt_x = ru_x + ru_w/2
        tt_y = ru_y - 0.26
        #title = f"BBP Benchmarking (REEB)"
        #tt_c = '#9F9D9C'
        #title_text = mpltext.Text(x=fx+tt_x*fs, y=fy+tt_y*fs, text=f'{title}', 
                                  #va="center", ha="center", color=tt_c, fontweight="normal", fontsize=12) #fontfamily='serif'
        
        #ax.add_artist(title_text)