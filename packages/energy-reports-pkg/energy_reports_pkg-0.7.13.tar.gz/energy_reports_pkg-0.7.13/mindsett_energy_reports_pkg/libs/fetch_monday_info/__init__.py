

from .sync_with_monday import sync_with_monday
from .load_cf_from_db import load_cf_from_db

def fetch_monday_info(engine, 
                        monday_token,
                        table_name_cache, 
                        table_columns_cache,
                        monday_board_id,
                        columns_concerned=None, 
                        email_prefix=None,
                        sync_monday=None):

    if sync_monday is None:
        sync_monday = True
    
    # get contacts from db
    df_monday = load_cf_from_db(engine, table_name_cache, table_columns_cache)

    if sync_monday:
        df_monday = sync_with_monday(engine, 
                                    df_monday,
                                    monday_token, 
                                    table_name_cache, 
                                    monday_board_id,
                                    columns_concerned=columns_concerned, 
                                    email_prefix=email_prefix)
    return df_monday