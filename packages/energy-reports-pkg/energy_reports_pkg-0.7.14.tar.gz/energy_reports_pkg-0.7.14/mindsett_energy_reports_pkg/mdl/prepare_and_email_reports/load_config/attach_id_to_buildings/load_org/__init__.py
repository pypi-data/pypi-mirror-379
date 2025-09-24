import pandas as pd

def load_org(engine, table_name):

    with engine.connect() as conn:

        query = f""" select id as org_id, name as org from {table_name} """ # meta.space_annotations

        df_org = pd.read_sql_query(query, con=conn) 

        df_org.org = df_org.org.str.strip()
        
    return df_org