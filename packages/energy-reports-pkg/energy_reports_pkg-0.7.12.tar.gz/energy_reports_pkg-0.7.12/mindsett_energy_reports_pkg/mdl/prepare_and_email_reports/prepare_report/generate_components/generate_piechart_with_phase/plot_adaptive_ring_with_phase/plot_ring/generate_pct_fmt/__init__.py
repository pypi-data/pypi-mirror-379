

def generate_pct_fmt(sr):
    total_before_adding_gap = sr.sum()
    ls_orig_pct = (sr/total_before_adding_gap).to_list()
    ls_orig_pct_fmt = ['{:.0f}%'.format(round(p*100)) for p in ls_orig_pct]
    ls_orig_pct_fmt.append('') # add for potential gap value
    return ls_orig_pct_fmt