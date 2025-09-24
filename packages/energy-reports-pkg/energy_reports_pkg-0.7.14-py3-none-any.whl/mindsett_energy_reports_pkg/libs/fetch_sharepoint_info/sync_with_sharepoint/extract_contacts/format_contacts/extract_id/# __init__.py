

def extract_id(x):

    # example value : '5515593330 - https://cloudfmgroup-company.monday.com/boards/5515593330'
    
    str_x = str(x)
    if ' - ' in str_x:
        return str_x.split(' - ')[0]
    else:
        return x