
from .extract_contacts import extract_contacts
from .cache_cf_to_db import cache_cf_to_db

def sync_with_sharepoint(engine, df_cfg_db, sharepoint, table_name_cache):

    df_cfg_shp = extract_contacts(sharepoint) # currently, we are getting the last_update time by directly querying the file, as it is relative quick
    # if needed in the future, a dedicated lighter get_last_update_time function can be designed, and the actual extraction processing can be conditional

    flag_reload_from_sharepoint = True

    if (df_cfg_db.shape[0] > 0) and (not df_cfg_db.last_update.isna().all()): # last_update was make null when the last_update_time was not available

        last_update_db  = df_cfg_db['last_update'].max()
        last_update_shp = df_cfg_shp['last_update'].max()
        # print(f'{last_update_shp=}')

        if last_update_db == last_update_shp: # here some efforts of writing to db can be saved if the cached data is already up-to-date.
            
            print('[INFO]: using config from the db cache as it is up-to-date!')
            flag_reload_from_sharepoint = False
        
    if flag_reload_from_sharepoint:

        # pass
        cache_cf_to_db(engine, table_name_cache, df_cfg_shp)

    return df_cfg_shp