

def annotate_pct_on_pies(ax, sr, ls_orig_pct_fmt, 
                        pct_hide=None,
                        pct_out=None):
    
    if pct_hide is None:
        pct_hide = 0.04

    if pct_out is None:
        pct_out = 0.065

    for index, pct_value in enumerate(sr.to_list()):

        ax.texts[index*2+1].update({"text": ls_orig_pct_fmt[index]})

        if abs(pct_value) < pct_hide * sr.sum(): 
            ax.texts[index*2+1].update({"text": ''})
        elif abs(pct_value) < pct_out * sr.sum(): 
            ax.texts[index*2].update({"text": f'{ax.texts[index*2+1].get_text()}'})
            ax.texts[index*2+1].update({"text": ''})