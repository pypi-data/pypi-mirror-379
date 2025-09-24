from datetime import timedelta
import pandas as pd
# from sqlalchemy import create_engine

from mdl.utils_ import enriching_time_features

def statement_for_avg_action_time(db, building_name, thing_name, start_time, end_time,
                                  action=1,
                                  period_freq_str='week'):

    

    time_restriction = f"""(time >= '{start_time}') and (time < '{end_time}')"""

    statement_list = [f""""root_name"='{building_name}'"""]
    statement_full = " and ".join(statement_list)

    query = f"""select time,action,root_name,thing_name from {db.table_on_off.name} where {statement_full} and {time_restriction};"""

    engine = db.engine

    with engine.connect() as conn:
        df_on_off = pd.read_sql_query(query, con=conn)

    df_on_off['thing_name'] = df_on_off['thing_name'].str.lstrip().str.rstrip("0123456789 ")

    df_on_off_selected = df_on_off.loc[df_on_off['thing_name']==thing_name]
    

    if df_on_off_selected.shape[0] > 0: # handle the  case that no on/off data is returned

        df_on_off_selected = enriching_time_features(df_on_off_selected)

        df_on_off_avg = df_on_off_selected.groupby(['action']).time_of_day_in_float.mean()

        avg_start_time = str(timedelta(hours=df_on_off_avg[action])).split('.')[0][:-3]

        # AM/PM to the time

        time_list = avg_start_time.split(":")

        hour_digit = int(time_list[0])
        if hour_digit < 12:
            letter = " AM" 
        else: 
            letter = " PM"
            if hour_digit >= 13:
                time_list[0] = str(hour_digit-12)

        time_list.append(letter)
        time_list[1] = ":"+time_list[1]
        avg_start_time_with_letter = "".join(time_list)   
        
        start_finish_dict = {1: 'start', -1: 'finish'}


        statement = f"{avg_start_time_with_letter} was the average {start_finish_dict[action]} time for the {thing_name} over this {period_freq_str}." # temp fix
    else: 
        statement = None
    
    return statement
