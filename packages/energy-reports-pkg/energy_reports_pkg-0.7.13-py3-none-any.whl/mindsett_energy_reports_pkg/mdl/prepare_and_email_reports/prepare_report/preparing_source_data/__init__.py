# from pathlib import Path
from os import path
import pandas as pd
from cache_return import cache_return

from mdl.utils_ import enriching_time_features
from mdl.utils_ import patch_missing_periods

# from .unify_db_interface import unify_db_interface
from .load_source_data import load_source_data

from .validate_data_not_empty import validate_data_not_empty
from .refine_group_name import refine_group_name
# from .patch_missing_periods import patch_missing_periods

@cache_return
def preparing_source_data(postgresdb, 
                          site_obj,
                          debug=False,
                          chunksize=10):
    
    # get the specific time for the individual site
    start_time = site_obj.get_start_time()
    start_time_co2_barchart = site_obj.get_start_time_co2_barchart()
    end_time = site_obj.get_end_time()
    schedule_records = site_obj.get_schedule_records(postgresdb)

    df_meta_with_value, df_meta_with_value_building = load_source_data(postgresdb, 
                                                                        start_time, 
                                                                        start_time_co2_barchart,
                                                                        end_time, 
                                                                        site_obj.building_id,
                                                                        chunksize=chunksize,
                                                                        exception=site_obj.exception,
                                                                        timezone=site_obj.timezone,
                                                                        caching=debug)
    
    # print('df_meta_with_value.shape: ', df_meta_with_value.shape)
    validate_data_not_empty(df_meta_with_value, df_meta_with_value_building)

    # print('df_meta_with_value.info: ', df_meta_with_value.info())

    df_meta_with_value = patch_missing_periods(df_meta_with_value, start_time, end_time,
                                                        time_col='time',
                                                        value_col='W',
                                                        period_freq=site_obj.period_freq,
                                                        timezone=site_obj.timezone)

    df_meta_with_value_building = patch_missing_periods(df_meta_with_value_building, start_time_co2_barchart, end_time,
                                                        time_col='time',
                                                        value_col='kwh',
                                                        period_freq=site_obj.period_freq,
                                                        timezone=site_obj.timezone)
    
    df_meta_with_value = refine_group_name(df_meta_with_value, 
                                           site_obj.asset_group, 
                                           site_obj.group_name_column_exchange, 
                                           site_obj.fillna_value,
                                           site_obj.group_name_modification)

    df_meta_with_value = enriching_time_features(df_meta_with_value, 
                                                    schedule_records= schedule_records,
                                                    period_freq=site_obj.period_freq,
                                                    weekend=site_obj.weekend, 
                                                    working_end_time=site_obj.working_end_time, 
                                                    working_start_time=site_obj.working_start_time,
                                                    timezone=site_obj.timezone)

    df_meta_with_value_building = enriching_time_features(df_meta_with_value_building,
                                                    schedule_records= schedule_records,
                                                    period_freq=site_obj.period_freq,
                                                    weekend=site_obj.weekend, 
                                                    working_end_time=site_obj.working_end_time, 
                                                    working_start_time=site_obj.working_start_time,
                                                    timezone=site_obj.timezone)
    
    # print('df_meta_with_value.shape: ', df_meta_with_value.shape)
    return df_meta_with_value, df_meta_with_value_building