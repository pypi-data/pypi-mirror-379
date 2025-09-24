


def get_formatted_arrow(pct_value):

    if pct_value > 0.005: 
            label_arrow_str = r'${\blacktriangle}$'

    elif pct_value < -0.005:
        label_arrow_str = r'$\:\!\triangledown\:\!$'

    else:
        label_arrow_str = r'$\!$--'
    
    label_arrow_pad = ' '
    label_arrow = label_arrow_pad + label_arrow_str

    return label_arrow