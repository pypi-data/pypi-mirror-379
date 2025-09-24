
from .load_building import load_building
from .load_org import load_org

from cache_return import cache_return

@cache_return
def attach_id_to_buildings(engine, df_config, table_org_name, table_building_name):

    df_org = load_org(engine, table_org_name)
    df_building = load_building(engine, table_building_name, caching=False)
    df_bld_org = df_building.merge(df_org, on='org_id', how='left').dropna()
    # df_config_bld_id = df_config.merge(df_bld_org, on=['building_name', 'org'], how='left')
    # df_config = df_config.drop(columns=['building_name', 'org'])
    df_config_bld_id = df_config.merge(df_bld_org, on='building_id', how='left')
    is_missing_bld_name = df_config_bld_id.building_id.isna().any()

    if is_missing_bld_name: # this part may not be very necessary after change the mergy on building_id
        df_config_bld_name_missing = df_config_bld_id.loc[df_config_bld_id['building_name'].isna()]

        missed_buildings = df_config_bld_name_missing['item_name'].to_list()
        raise Exception(f"The name(s) for building id(s) {missed_buildings} cannot be found!")

    return df_config_bld_id.drop(columns=['item_name', 'group_name'])
