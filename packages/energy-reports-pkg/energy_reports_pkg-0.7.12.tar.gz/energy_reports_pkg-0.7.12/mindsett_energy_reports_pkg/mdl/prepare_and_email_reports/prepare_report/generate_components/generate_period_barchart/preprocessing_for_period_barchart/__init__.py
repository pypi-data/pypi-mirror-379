import pandas as pd
from itertools import product

from .patch_missing_ooh_periods_sign import patch_missing_ooh_periods_sign

def preprocessing_for_period_barchart(df_meta_with_value,
                                      sign_column=None,
                                        period_column=None, 
                                        ooh_column=None, 
                                        kwh_column=None,
                                        no_of_period=None):
    if sign_column is None:
        sign_column = 'neg_sign'

    if period_column is None:
        period_column = "period"
    
    if ooh_column is None:
        ooh_column = "out_of_hours"

    if  kwh_column is None:
        kwh_column = "kwh"

    if no_of_period is None:
        no_of_period = 6

    df_meta_with_value[sign_column] = df_meta_with_value[kwh_column].lt(0)

    df_grouped_working_hours_period = df_meta_with_value.groupby([sign_column, period_column, ooh_column])[kwh_column].sum()

    period_max = df_meta_with_value[period_column].max() # todo: check whether there are other better ways for getting the max period, as it might be missing also

    # handle the situation that not all groups exist
    df_grouped_working_hours_period = patch_missing_ooh_periods_sign(df_grouped_working_hours_period, period_max,
                                                                    no_of_period=no_of_period)

    df_grouped_working_hours_period_unstacked = df_grouped_working_hours_period.unstack([sign_column, ooh_column])
    df_grouped_working_hours_period_unstacked = df_grouped_working_hours_period_unstacked.sort_index()

    # convert the unit from kwh to mwh
    df_grouped_working_hours_period_unstacked = df_grouped_working_hours_period_unstacked.div(1000)
    
    return df_grouped_working_hours_period_unstacked