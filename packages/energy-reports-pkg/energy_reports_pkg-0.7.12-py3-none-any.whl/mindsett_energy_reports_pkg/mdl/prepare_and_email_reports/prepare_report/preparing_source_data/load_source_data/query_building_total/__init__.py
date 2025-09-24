import pandas as pd

def query_building_total(db, start_time, end_time, building_id, 
                        #  organisation=None,
                         timezone='UTC'):

    query_start_time = pd.Timestamp(start_time, tz=timezone)
    query_end_time  =  pd.Timestamp(end_time, tz=timezone)

    query_start_time_str = query_start_time.strftime("%Y-%m-%d %H:%M:%S.%f%z")
    query_end_time_str   = query_end_time.strftime("%Y-%m-%d %H:%M:%S.%f%z")

    # print('query_start_time_str: ', query_start_time_str)
    # print('query_end_time_str: ', query_end_time_str)


    time_period = f"""(time >= '{query_start_time_str}') and (time < '{query_end_time_str}')"""

    statement_list = [f"""building_id = '{building_id}'"""]
    
    # if organisation != None:
    #     statement_new = f"""btrim("organisation") = '{organisation}'"""
    #     statement_list.append(statement_new)

    statement_full = ' and '.join(statement_list)

    query = f"""select time, kwh from {db.table_building_total.name} where {statement_full} and {time_period};"""

    # year, month, building_name, organisation, building_id, org_id

    # print('building_total query: ', query)

    engine = db.engine 

    with engine.connect() as conn:
    
        df_meta_with_value = pd.read_sql_query(query, con=conn)


    return df_meta_with_value