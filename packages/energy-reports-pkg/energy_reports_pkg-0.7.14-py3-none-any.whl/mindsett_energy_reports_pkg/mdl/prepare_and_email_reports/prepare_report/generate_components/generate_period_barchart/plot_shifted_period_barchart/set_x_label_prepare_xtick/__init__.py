
import matplotlib.pyplot as plt


def set_x_label_prepare_xtick(ax, df_grouped_working_hours_period_unstacked, 
                              fontsize=None):
    
    if fontsize is None:
        fontsize = 13

    if df_grouped_working_hours_period_unstacked.index.freqstr == 'M':
        x_ticks_labels = df_grouped_working_hours_period_unstacked.index.strftime("%b %y").tolist()
        ax.set_xlabel("Month", labelpad = 13, fontsize = fontsize)
        plt.xticks(rotation=45) # please note: plt cannot be replace by ax, as it will throw errors
    else:
        ls_week_str = (df_grouped_working_hours_period_unstacked.index).strftime("%W").tolist()
        x_ticks_labels = [f"{(int(week)+1):02d}" for week in ls_week_str]   # add 1 week to the current_period_obj so that the start week is not Week 00
        ax.set_xlabel("Week Number", labelpad = 13, fontsize = fontsize)
        plt.xticks(rotation=0)

    x_ticks_labels.insert(0,"")
    x_ticks_labels.append("")

    return x_ticks_labels