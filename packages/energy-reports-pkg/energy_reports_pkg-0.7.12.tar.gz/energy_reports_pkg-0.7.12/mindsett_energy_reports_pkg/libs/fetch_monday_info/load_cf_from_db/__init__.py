
import pandas as pd


def load_cf_from_db(engine, table_name_cache, columns):

    columns_str = ', '.join(columns)

    cache_query = f"""select {columns_str} from {table_name_cache};"""

    with engine.connect() as conn:
        df_cache = pd.read_sql_query(cache_query, con=conn)

    if df_cache.shape[0] > 0:
        df_cache.mailing_list = df_cache.mailing_list.apply(lambda x: x[1:-1].split(','))

    return df_cache