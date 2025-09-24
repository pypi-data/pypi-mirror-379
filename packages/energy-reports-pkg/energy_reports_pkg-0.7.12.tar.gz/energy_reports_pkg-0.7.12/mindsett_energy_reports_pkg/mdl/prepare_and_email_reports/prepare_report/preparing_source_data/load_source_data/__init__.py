from os import path
import pandas as pd

from .query_building_total import query_building_total
from .import_data_with_meta_postgres import import_data_with_meta_postgres

from cache_return import cache_return

@cache_return
def load_source_data(postgresdb, 
                     start_time, 
                     start_time_co2_barchart,
                     end_time, 
                     building_id,
                     exception=None,
                     chunksize=10,
                     timezone='UTC'):

    df_meta_with_value = import_data_with_meta_postgres(postgresdb, 
                                                            start_time, 
                                                            end_time, 
                                                            building_id,
                                                            exception=exception,
                                                            chunksize=chunksize,
                                                            timezone=timezone)
    df_meta_with_value_building = query_building_total(postgresdb, 
                                                        start_time=start_time_co2_barchart,
                                                        end_time=end_time, 
                                                        building_id=building_id, # please note that this is a postition arg
                                                        timezone=timezone)
    
    return df_meta_with_value, df_meta_with_value_building