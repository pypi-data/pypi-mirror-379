import pandas as pd

def load_energy_price(engine, table_name):

    with engine.connect() as conn:

        query = f"""select space_id as building_id, price*1000 as conv_mwh_price, start as start_time from {table_name};""" # meta.space_annotations
        df_price_all = pd.read_sql_query(query, con=conn) 
    
    df_price_latest = df_price_all.loc[df_price_all.groupby('building_id').start_time.idxmax()].drop(columns='start_time')
        
    return df_price_latest

# def load_energy_price():
