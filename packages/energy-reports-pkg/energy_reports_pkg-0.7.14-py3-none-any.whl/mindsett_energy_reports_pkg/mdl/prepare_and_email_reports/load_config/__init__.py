
from fetch_sharepoint_info import fetch_sharepoint_info

from .check_and_keep_valid import check_and_keep_valid
from .load_timezone import load_timezone
from .load_sqm import load_sqm
from .attach_id_to_buildings import attach_id_to_buildings
from .apply_price_from_db import apply_price_from_db

def load_config(engine, 
                sharepoint,
                table_name_org,
                table_name_building,
                table_name_timezone, 
                table_name_sqm,
                table_name_price,
                table_name_cache, 
                table_columns_cache,
                monday=None, # making if optional here, so in the future it can be ignored from the outer layer of functions
                sync_source=None,
                cfg_src_type=None):
    
    if cfg_src_type is None:
         cfg_src_type = 'sharepoint' # default to sharepoint as suggested by Pat


    if cfg_src_type == 'sharepoint':
         
         df_config_raw = fetch_sharepoint_info(engine, 
                                                sharepoint, 
                                                table_name_cache, 
                                                table_columns_cache,
                                                sync_source=sync_source)
    
    elif cfg_src_type == 'monday': 

        from fetch_monday_info import fetch_monday_info

        if monday is None:
             raise Exception('[ERROR]: the config for monday is not provided, but cfg_src_type is monday!')

        df_config_raw = fetch_monday_info(engine, 
                                    monday.auth.TOKEN,
                                    table_name_cache, 
                                    table_columns_cache,
                                    monday.board_id,
                                    columns_concerned=monday.columns_concerned, 
                                    email_prefix=monday.email_prefix,
                                    sync_monday=sync_source)
    
    else:
        raise Exception('[ERROR]: please choose the cfg_src_type from options [sharepoint, monday].')

        
    df_config = attach_id_to_buildings(engine, df_config_raw, table_name_org, table_name_building, 
                                       caching=False) # df_config has to be the same name, so not renaming it here

    df_tz = load_timezone(engine, table_name_timezone)
    df_config_tz = df_config.merge(df_tz, on='building_id', how='left')

    df_sqm = load_sqm(engine, table_name_sqm)
    df_config_tz_sqm = df_config_tz.merge(df_sqm, on='building_id', how='left')

    df_config_tz_price = apply_price_from_db(engine, table_name_price, df_config_tz_sqm)
    # df_price = load_energy_price(engine, table_name_price)
    # df_config_tz_sqm = df_config_tz_sqm.rename(columns={'conv_mwh_price': 'conv_mwh_price_bak'})
    # # df_config_tz_sqm_no_price = df_config_tz_sqm.drop(columns=['conv_mwh_price'])
    # df_config_tz_price = df_config_tz_sqm.merge(df_price, on='building_id', how='left')
    # df_config_tz_price['conv_mwh_price'] = df_config_tz_price['conv_mwh_price'].fillna(df_config_tz_price['conv_mwh_price_bak'])
    # df_config_tz_price = df_config_tz_price.drop(columns=['conv_mwh_price_bak'])
    
    df_config_vld = check_and_keep_valid(df_config_tz_price)
    
    return df_config_vld
        