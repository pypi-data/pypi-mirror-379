
import pandas as pd


def get_schedule_records(self, db_schedule):

    # print(f'self.site_name: "{self.site_name}"')
    # print(f'self.org_name: "{self.org_name}"')

    statement_list = [f"""bs.id = '{self.building_id}'"""]

    if self.org_name is not None:
        statement_new  = f"""os.id = '{self.org_id}'"""
        statement_list.append(statement_new)
    statement_full = " and ".join(statement_list)

    engine = db_schedule.engine # new installation - The Hub - ENGINE_WH

    with engine.connect() as conn:
        query = f"""select ss.day
                    ,ss.name
                    ,ss.start_time
                    ,ss.end_time
                    ,BTRIM(bs.name) as site_name 
                    ,BTRIM(os.name) as organisation
                    from {db_schedule.table_schedule.name} ss
                    join {db_schedule.table_building.name} bs on ss.space_id = bs.id
                    join {db_schedule.table_org.name} os on bs.org_id = os.id
                    where {statement_full};"""
        df_schedule = pd.read_sql_query(query,
                                        con=conn) #new installation - The Hub - table_name_wh
        
        # print("schedule_query: ", query)
    return df_schedule.to_dict('records')