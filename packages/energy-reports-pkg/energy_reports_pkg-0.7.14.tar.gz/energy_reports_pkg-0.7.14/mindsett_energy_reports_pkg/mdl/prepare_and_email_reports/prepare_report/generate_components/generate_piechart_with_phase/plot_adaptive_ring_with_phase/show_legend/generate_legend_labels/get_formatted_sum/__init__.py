

def get_formatted_sum(value, 
                     sum_value_len=None):
    
    if sum_value_len is None:
        sum_value_len = 8

    # adjust the decimal point and the unit based on the actual value
    sum_abs = abs(value)
    if sum_abs >= 99_950: # KWH
        label_kwh_str = f'{value/1000:4.0f} MWh'
    elif sum_abs >= 1000: # KWH
        label_kwh_str = f'{value/1000:4.1f} MWh'
    elif sum_abs >= 99.95: # KWH 
        label_kwh_str = f'{value:4.0f} KWh' # to handle the case that (sum_abs:  99.98276) => (100.0 KWh)
    elif sum_abs >= 1:
        label_kwh_str = f'{value:4.1f} KWh'
    elif sum_abs >= 0.09995:
        label_kwh_str = f'{value*1000:4.0f} Wh'
    else:
        label_kwh_str = f'{value*1000:4.1f} Wh'

    label_kwh_str_strip = label_kwh_str.strip()

    label_kwh_pad_digi = ' ' *int((sum_value_len - len(label_kwh_str_strip))*2)
    label_kwh_pad_dot = ' '*label_kwh_str_strip.count('.')

    label_kwh = label_kwh_pad_dot + label_kwh_pad_digi + label_kwh_str_strip + ','

    return label_kwh