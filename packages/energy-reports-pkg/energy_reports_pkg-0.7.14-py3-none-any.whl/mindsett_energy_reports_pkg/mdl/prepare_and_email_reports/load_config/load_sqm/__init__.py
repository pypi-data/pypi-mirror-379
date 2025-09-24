import pandas as pd

def load_sqm(engine, table_name):

    with engine.connect() as conn:

        query = f""" select space_id as building_id, sqm as floor_size  from {table_name};""" # meta.space_annotations

        df_tz = pd.read_sql_query(query, con=conn) 
        
    return df_tz