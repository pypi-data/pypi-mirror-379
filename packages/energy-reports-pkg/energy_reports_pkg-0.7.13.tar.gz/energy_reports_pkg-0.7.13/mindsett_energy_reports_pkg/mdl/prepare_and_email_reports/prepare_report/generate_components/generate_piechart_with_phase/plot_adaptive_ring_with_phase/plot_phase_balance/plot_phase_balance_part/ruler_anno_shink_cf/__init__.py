

# ruler annotation shinking config

config_dict = {'full_name': {'size_lim': 0.11*2, 
                             'names': {'part_one': "", 
                                       'part_two': '', 
                                       'part_three': ''}},
               'short_name':  {'size_lim': 0.035*2, 
                               'names': {'part_one': "", 
                                       'part_two': '', 
                                       'part_three': ''}},
               'null_name':  {'size_lim': 0.03*2, 
                              'names': {'part_one': "", 
                                        'part_two': '', 
                                        'part_three': ''}},
               }


def ruler_anno_shink_cf(bar_width, part):

    if bar_width > config_dict['full_name']['size_lim']:
        rpa_text = config_dict['full_name']['names'][part]
    elif bar_width > config_dict['short_name']['size_lim']:
        rpa_text = config_dict['short_name']['names'][part]
    else:
        rpa_text = config_dict['null_name']['names'][part]

    return rpa_text
