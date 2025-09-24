
import pandas as pd
from tqdm import tqdm

from .load_iot_data_partition import load_iot_data_partition

def load_iot_data(engine, time_range, iot_table_name, id_list, chunksize=10):

    # time_partition_list = generate_time_partition_list(time_range, freq=partition_freq)

    df_iot = pd.DataFrame([])

    id_list_partitions = [id_list[x:x+chunksize] for x in range(0, len(id_list), chunksize)]

    no_partition = len(id_list_partitions)

    # for id_list_part in tqdm(id_list_partitions):
    for batch, id_list_part in enumerate(id_list_partitions):

        print(f'batch: {batch+1}/{no_partition}')
        df_iot_part = load_iot_data_partition(engine, time_range, iot_table_name, id_list_part)
        # df_iot_part = load_iot_data_partition(engine, time_partition, iot_table_name, meta_table_name, statement_full)

        df_iot = pd.concat([df_iot, df_iot_part])
        
    return df_iot

    # load_iot_data_partition(engine, time_partition, iot_table_name, meta_table_name, statement_full)