import pandas as pd

from .generate_day_code_list import generate_day_code_list


def generate_day_code(df_pivot_working_hours):
    
    datetime_list = list(pd.to_datetime(df_pivot_working_hours.index))

    day_code_list = generate_day_code_list(datetime_list)

    day_code_list.insert(0,"") # for making spaces at the start
    day_code_list.insert(0,"")
    # day_code_list.insert(0,"")
    day_code_list.append("") # for making spaces at the end
    day_code_list.append("")

    return day_code_list