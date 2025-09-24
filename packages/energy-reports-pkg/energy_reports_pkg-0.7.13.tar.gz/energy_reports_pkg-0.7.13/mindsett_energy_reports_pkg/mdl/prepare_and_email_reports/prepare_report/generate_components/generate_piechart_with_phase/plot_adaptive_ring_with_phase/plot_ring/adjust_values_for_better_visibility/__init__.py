

def adjust_values_for_better_visibility(sr_orig,
                                        thres_invisibity=0.01,
                                        adjustment_pct=0.01):

    # ensure that the pct is positive 
    sr_orig_abs = sr_orig.abs()
    sr_plot_pct = sr_orig_abs/sr_orig_abs.sum()

    # print(f'{sr_plot_pct = }')

    # label the non-visible
    non_visible_index = sr_plot_pct.loc[sr_plot_pct<thres_invisibity].index
    all_visible_index = sr_plot_pct.index.difference(non_visible_index)

    # slightly adjust the values to make the non-visible ones more visible
    previous_non_visiable_pct = sr_plot_pct.loc[non_visible_index].sum()
    sr_plot_pct.loc[non_visible_index] = sr_plot_pct.loc[non_visible_index] + adjustment_pct
    improved_non_visiable_pct = sr_plot_pct.loc[non_visible_index].sum()

    sr_plot_pct.loc[all_visible_index] = sr_plot_pct.loc[all_visible_index] * (1-improved_non_visiable_pct)/(1-previous_non_visiable_pct)

    # get the adjusted sum values for plots
    sr_plot_sum = sr_plot_pct * sr_orig.sum()

    return sr_plot_sum