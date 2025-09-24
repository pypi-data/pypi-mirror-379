

# ruler annotation shinking config

config_dict = {'full_name': {'size_lim': 0.11, 
                             'names': {'part_one': "L1", 
                                       'part_two': 'L2', 
                                       'part_three': 'L3'}},
               'shrink_name':  {'size_lim': 0.08, 
                                'names': {'part_one': "L1", 
                                       'part_two': 'L2', 
                                       'part_three': 'L3'}},
               'short_name':  {'size_lim': 0.06, 
                               'names': {'part_one': "1", 
                                       'part_two': '2', 
                                       'part_three': '3'}},
               'null_name':  {'size_lim': 0.05, 
                              'names': {'part_one': "", 
                                        'part_two': '', 
                                        'part_three': ''}},
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
