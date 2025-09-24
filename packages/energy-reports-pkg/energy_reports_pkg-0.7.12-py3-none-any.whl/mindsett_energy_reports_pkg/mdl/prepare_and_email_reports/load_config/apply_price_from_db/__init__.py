
from .load_energy_price import load_energy_price

def apply_price_from_db(engine, table_name_price, df_config_tz_sqm):

    df_price = load_energy_price(engine, table_name_price)
    df_config_tz_sqm = df_config_tz_sqm.rename(columns={'conv_mwh_price': 'conv_mwh_price_bak'})
    # df_config_tz_sqm_no_price = df_config_tz_sqm.drop(columns=['conv_mwh_price'])
    df_config_tz_price = df_config_tz_sqm.merge(df_price, on='building_id', how='left')
    df_config_tz_price['conv_mwh_price'] = df_config_tz_price['conv_mwh_price'].fillna(df_config_tz_price['conv_mwh_price_bak'])
    df_config_tz_price = df_config_tz_price.drop(columns=['conv_mwh_price_bak'])

    return df_config_tz_price