

def group_and_pivot(df_meta_with_value, 
                    asset_group=None,
                    reading_interval_in_mins=None):

    if asset_group is None:
        asset_group = 'thing_category'

    if reading_interval_in_mins is None:
        reading_interval_in_mins=10

    # Conversion into MWh
    w_to_kw_para = 1./1000
    min_to_hour_para = 1./60

    wm_to_kwh_parameter = w_to_kw_para * min_to_hour_para
    reading_to_kwh_parameter = reading_interval_in_mins * wm_to_kwh_parameter

    # group and pivot operation
    sr_pivot_asset_class = df_meta_with_value.groupby([asset_group, "period"])["W"].sum() * reading_to_kwh_parameter
    df_pivot_asset_group_by_period = sr_pivot_asset_class.unstack(["period"])

    return df_pivot_asset_group_by_period