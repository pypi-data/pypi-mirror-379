
import pandas as pd

from .get_meta_statement import get_meta_statement

def load_metadata(engine, table_name_meta, building_id, 
                #   organisation=None,  
                  exception=None):

    statement_full = get_meta_statement(building_id, 
                    #    organisation=organisation, 
                       exception=exception, # the filter will be applied to link type
                      )
    
    # print('statement_full: ', statement_full)

    meta_query = f"""select id, 
                            org,
                            building_name,
                            thing_name, 
                            thing_type, 
                            thing_category,
                            variable,
                            phase,
                            nid,
                            channel,
                            hardware_id
                            from {table_name_meta} 
                            where {statement_full};"""

    with engine.connect() as conn:
        df_meta = pd.read_sql_query(meta_query, con=conn)

    return df_meta