
from .append_df_to_table import append_df_to_table
from .empty_table import empty_table

def cache_cf_to_db(engine, table_name_cache, df_config):

    empty_table(engine, table_name_cache, with_log=False)
    append_df_to_table(engine, table_name_cache, df_config)

    return

