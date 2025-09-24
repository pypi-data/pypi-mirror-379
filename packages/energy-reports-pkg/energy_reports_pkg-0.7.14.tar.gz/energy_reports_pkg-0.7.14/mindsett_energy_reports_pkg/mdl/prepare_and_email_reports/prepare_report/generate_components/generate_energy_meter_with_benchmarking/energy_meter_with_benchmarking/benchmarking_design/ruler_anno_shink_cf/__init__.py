

# ruler annotation shinking config

config_dict = {'full_name': {'size_lim': 0.11, 'names': {'part_one': "GOOD", 'part_two': 'NORM', 'part_three': 'POOR'}},
                       'shrink_name':  {'size_lim': 0.08, 'names': {'part_one': "GD", 'part_two': 'NR', 'part_three': 'PR'}},
                       'short_name':  {'size_lim': 0.06, 'names': {'part_one': "G", 'part_two': 'N', 'part_three': 'P'}},
                       'null_name':  {'size_lim': 0.05, 'names': {'part_one': "", 'part_two': '', 'part_three': ''}},
}

def ruler_anno_shink_cf(bar_width, part):

    if bar_width > config_dict['full_name']['size_lim']:
        rpa_text = config_dict['full_name']['names'][part]
    elif bar_width > config_dict['shrink_name']['size_lim']:
        rpa_text = config_dict['shrink_name']['names'][part]
    elif bar_width > config_dict['short_name']['size_lim']:
        rpa_text = config_dict['short_name']['names'][part]
    else:
        rpa_text = config_dict['null_name']['names'][part]
    
    return rpa_text


