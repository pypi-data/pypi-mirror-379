
import pandas as pd
from itertools import product

def patch_missing_ooh_periods_sign(df_grouped_working_hours_period,
                                  period_max,
                                  no_of_period=None):
    
    if no_of_period is None:
        no_of_period = 6

    # handle the situation that not all groups exist
    expected_sign = [True, False]
    expected_periods = [period_max-i for i in range(no_of_period)]
    expected_working_hours = [True, False]
    expected_group_index = pd.Index(product(expected_sign, expected_periods, expected_working_hours))

    missing_group_index = expected_group_index.drop(df_grouped_working_hours_period.index)

    for indice in missing_group_index:
        df_grouped_working_hours_period.loc[indice] = 0

    return df_grouped_working_hours_period