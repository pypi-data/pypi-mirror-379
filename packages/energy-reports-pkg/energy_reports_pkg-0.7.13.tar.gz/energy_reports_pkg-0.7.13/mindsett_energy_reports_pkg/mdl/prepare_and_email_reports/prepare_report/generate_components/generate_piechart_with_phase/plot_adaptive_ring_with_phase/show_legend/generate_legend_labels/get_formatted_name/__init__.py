

def get_formatted_name(name_text, 
                       max_len=None):
    
    if max_len is None:
        max_len = 15

    if len(name_text) > max_len:
        label_name = name_text[:(max_len-3)]+"..."
    else:   
        label_name = name_text

    return label_name