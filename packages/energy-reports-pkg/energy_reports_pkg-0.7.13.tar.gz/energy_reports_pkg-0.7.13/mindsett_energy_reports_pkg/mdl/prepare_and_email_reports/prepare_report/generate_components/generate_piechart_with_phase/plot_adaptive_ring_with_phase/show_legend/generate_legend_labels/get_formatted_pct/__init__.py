


def get_formatted_pct(pct_value, 
                      pct_len=None):
    
    if pct_len is None:
        pct_len = 2

    # format the relative change

    pad_for_3_digit = 1

    if abs(pct_value) <= 1.06:
        label_pct_str = str(round(abs(pct_value)*100))
        label_pct_unit = r"%"
        label_pct_dot = " "*label_pct_str.count('.')
        label_pct_pad = ' ' *int((pct_len - len(label_pct_str))*2 + pad_for_3_digit) 
    elif abs(pct_value) < 1000:
        label_pct_str = str(round(abs(pct_value))) # todo: config number of decimals
        if len(label_pct_str) < 2:
            label_pct_str = str(round(abs(pct_value)*10)/10) # add one decimal
        label_pct_unit = r"X"
        label_pct_dot = " "*label_pct_str.count('.')
        label_pct_pad = ' ' *int((pct_len - len(label_pct_str))*2 +1 + pad_for_3_digit)
    elif abs(pct_value) < 1000_000:
        label_pct_str = str(round(abs(pct_value)/1000)) # todo: config number of decimals
        if len(label_pct_str) < 2:
            label_pct_str = str(round(abs(pct_value)/1000*10)/10) # add one decimal
        label_pct_unit = r"KX"
        label_pct_dot = " "*label_pct_str.count('.')
        label_pct_pad = ' ' *int((pct_len - len(label_pct_str))*2 -1 + pad_for_3_digit)
    else:
        label_pct_str = str(round(abs(pct_value)/1000_000)) # todo: config number of decimals
        if len(label_pct_str) < 2:
            label_pct_str = str(round(abs(pct_value)/1000_1000*10)/10) # add one decimal
        label_pct_unit = r"MX"
        label_pct_dot = " "*label_pct_str.count('.')
        label_pct_pad = ' ' *int((pct_len - len(label_pct_str))*2 -2 + pad_for_3_digit)

    # print(f'label_pct_pad = "{label_pct_pad}"')
    label_pct = label_pct_dot + label_pct_pad + label_pct_str + label_pct_unit + ',' + ' ' * 5

    return label_pct