
from .load_cf_from_db import load_cf_from_db
from .sync_with_sharepoint import sync_with_sharepoint

def fetch_sharepoint_info(engine, 
                          sharepoint, 
                          table_name_cache, 
                          table_columns_cache,
                          sync_source=None):

    if sync_source is None:
        sync_source = True

    # get contacts/configs from the db
    df_cfg_db = load_cf_from_db(engine, table_name_cache, table_columns_cache)

    # print(f'{df_cfg_db.info()=}')

    if sync_source:
        df_cfg = sync_with_sharepoint(engine, 
                                    df_cfg_db, 
                                    sharepoint, 
                                    table_name_cache)
    else:
        df_cfg = df_cfg_db

    return df_cfg