import pandas as pd

from cache_return import cache_return

@cache_return
def load_building(engine, table_name):

    with engine.connect() as conn:

        query = f""" select id as building_id
                            ,name as building_name
                            ,org_id
                            from {table_name} """ # meta.space_annotations

        df_building = pd.read_sql_query(query, con=conn) 

        df_building.building_name = df_building.building_name.str.strip()
        
    return df_building