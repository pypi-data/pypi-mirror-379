



def groupby_date_and_ooh_current_period(df_meta_with_value):

    # select data only for the current period

    period_current = df_meta_with_value["period"].max()
    df_meta_with_value_current = df_meta_with_value.loc[df_meta_with_value["period"]==period_current]

    df_meta_with_value_current['neg_sign'] = df_meta_with_value_current['W'].lt(0)

    # Conversion into MWh
    w_to_mw_para = 1./1000/1000
    min_to_hour_para = 1./60
    reading_interval_in_mins=10

    wm_to_mwh_parameter = w_to_mw_para * min_to_hour_para
    reading_to_mwh_parameter = reading_interval_in_mins * wm_to_mwh_parameter

    # Conversion into MWh
    # reading_to_mwh_parameter = 1./1000

    # todo: Better to change to df_meta_value_building
    df_grouped_working_hours_current_period_with_sign = df_meta_with_value_current.groupby(['neg_sign', "date", 'out_of_hours'])["W"].sum() * reading_to_mwh_parameter  # Div 1000 for convertion to MWh

    # df_grouped_working_hours_current_period = df_grouped_working_hours_current_period_with_sign.droplevel('neg_sign')
    # # select only the maximum period
    # df_grouped_working_hours_multiple_period_unstack = df_grouped_working_hours_multiple_period.unstack(["period"])
    # period_current = df_grouped_working_hours_multiple_period_unstack.columns[-1]
    # df_grouped_working_hours = df_grouped_working_hours_multiple_period_unstack.loc[:, period_current]

    # todo: fill missing group index
    df_pivot_working_hours_with_sign_sorted = df_grouped_working_hours_current_period_with_sign.unstack(['neg_sign', 'out_of_hours']).sort_index(axis=1, 
                                                                                                                 level=1, 
                                                                                                                 ascending=False)
    
    return df_pivot_working_hours_with_sign_sorted, period_current