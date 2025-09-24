
from .append_df_to_table import append_df_to_table
from mdl.utils_ import empty_table

def cache_df_to_db(engine, table_name, df):

    empty_table(engine, table_name, with_log=False)
    append_df_to_table(engine, table_name, df)

    return

