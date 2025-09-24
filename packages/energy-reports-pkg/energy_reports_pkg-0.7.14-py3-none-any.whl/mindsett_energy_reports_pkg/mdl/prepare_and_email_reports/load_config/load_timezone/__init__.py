import pandas as pd

def load_timezone(engine, table_name):

    with engine.connect() as conn:

        query = f""" select space_id as building_id, value as timezone  from {table_name} where key ='timezone' """ # meta.space_annotations

        df_tz = pd.read_sql_query(query, con=conn) 
        
    return df_tz