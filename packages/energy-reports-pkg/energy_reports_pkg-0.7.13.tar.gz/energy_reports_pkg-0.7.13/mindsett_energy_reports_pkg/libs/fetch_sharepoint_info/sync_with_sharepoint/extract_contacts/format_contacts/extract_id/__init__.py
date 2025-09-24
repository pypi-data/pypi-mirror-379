

def extract_id(x):

    # example value : '5515593330 - https://cloudfmgroup-company.monday.com/boards/5515593330'

    # if isinstance(x, float):
    #     x = int(x)

    str_x = str(x)
    if ' - ' in str_x:
        id_str = str_x.split(' - ')[0]
    else:
        id_str =  str_x
    
    if id_str == 'nan':
        return None
    else:
        return id_str.split('.')[0] # there might be the case that it's converted from float with . e.g. 8370787257.0