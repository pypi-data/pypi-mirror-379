import pandas as pd

from .load_metadata import load_metadata
from .load_iot_data import load_iot_data

def import_data_with_meta_postgres(db, start_time, end_time, building_id, 
                        #   organisation=None, 
                          exception=None,
                          chunksize=10,
                          # meta_columns_for_join=['nid', 'channel_number'],
                          # iot_columns_for_join=['nid', 'channel'],
                          # reading_interval_in_mins=10,
                          timezone='UTC'):  # the resampling operation should be implemented later

    # format the time range
    query_start_time = pd.Timestamp(start_time, tz=timezone)
    query_end_time  =  pd.Timestamp(end_time, tz=timezone)

    query_start_time_str = query_start_time.strftime("%Y-%m-%d %H:%M:%S.%f%z")
    query_end_time_str   = query_end_time.strftime("%Y-%m-%d %H:%M:%S.%f%z")

    time_range = [query_start_time_str, query_end_time_str]

    engine = db.engine
    table_name_iot = db.table_iot.name
    table_name_meta = db.table_meta.name
    # table_name_link = db.table_name_link

    df_meta = load_metadata(engine, table_name_meta, building_id, 
                            # organisation=organisation,
                            exception=exception)

    if df_meta.shape[0] == 0:

        raise Exception('There is not metadata found for this building!')

    # print('df_meta: ', df_meta)

    id_list = df_meta.id.to_list()

    df_emd = load_iot_data(engine, time_range, table_name_iot, id_list, chunksize=chunksize)

    df_meta_with_value = df_emd.merge(df_meta, on='id').drop(columns=['id']).rename(columns={'w': 'W'})

    # print('df_meta_with_value.shape: ', df_meta_with_value.shape)

    return df_meta_with_value