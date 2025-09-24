
import pandas as pd

def load_iot_data_partition(engine, time_range, iot_table_name, id_list_part):

    time_condition = f""" ((time >= '{time_range[0]}') and (time < '{time_range[1]}')) """

    id_list_str = str(tuple(id_list_part)).replace('),)', '))')

    data_query = f"""select time, id, kwh*6000 as W from {iot_table_name} 
                where id in {id_list_str}
                    and {time_condition};"""

    # print('data_query: ', data_query)

    with engine.connect() as conn:
        df_iot_part_iter = pd.read_sql_query(data_query, con=conn, chunksize=5000)

    df_iot_part = pd.DataFrame([])

    for df_iot_part_i in df_iot_part_iter:
        df_iot_part = pd.concat([df_iot_part, df_iot_part_i])

    return df_iot_part