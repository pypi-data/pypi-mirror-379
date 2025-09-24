
from .statement_for_biggest_ooh import statement_for_biggest_ooh
from .statement_for_total_ooh import statement_for_total_ooh
from .statement_for_avg_action_time import statement_for_avg_action_time


def insight_statements(db, df_for_statements, df_meta_with_value, period_freq_str='week'):   #df_meta_with_value is only used to get metadata information
    
    statements_list = []

    statement_str_total_ooh = statement_for_total_ooh(df_for_statements, 
                                                      period_freq_str=period_freq_str)
    statements_list.append(statement_str_total_ooh)

    # preparation for the third statement

    thing_name = 'Pizza Oven'
    
    if thing_name in df_meta_with_value['thing_name'].str.lstrip().str.rstrip("0123456789 ").unique():

        building_name = df_meta_with_value['building_name'].unique()[0]
        max_period = df_meta_with_value["period"].max()
        start_time_str = max_period.start_time
        end_time_str = max_period.end_time

        statement_str_avg_action_time = statement_for_avg_action_time(db, building_name, thing_name, start_time_str, end_time_str,
                                                                      action=1, 
                                                                      period_freq_str=period_freq_str) # None will be returned if no on/off data is found
        if statement_str_avg_action_time  is not None: 

            statements_list.append(statement_str_avg_action_time)

    # Statement for biggest OOH

    # print('df_for_statements: ', df_for_statements)

    statement_str_biggest_ooh = statement_for_biggest_ooh(df_for_statements, 
                                                          period_freq_str=period_freq_str)
    statements_list.append(statement_str_biggest_ooh)
        
    return statements_list