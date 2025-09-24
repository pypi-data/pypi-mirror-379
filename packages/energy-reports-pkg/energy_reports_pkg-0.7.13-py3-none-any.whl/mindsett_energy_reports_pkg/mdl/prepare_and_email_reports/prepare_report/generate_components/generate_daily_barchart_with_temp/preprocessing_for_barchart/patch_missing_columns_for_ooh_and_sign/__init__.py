
import pandas as pd

def patch_missing_columns_for_ooh_and_sign(df_pivot_working_hours_with_sign):

    columns_for_sign = [True, False]
    columns_for_ooh = [True, False]

    required_columns_for_ooh_and_sign = pd.MultiIndex.from_product([columns_for_sign, columns_for_ooh])

    # required_columns_for_ooh = [True, False]
    existing_columns_for_ooh_and_sign = df_pivot_working_hours_with_sign.columns

    for column in required_columns_for_ooh_and_sign:
        if column not in existing_columns_for_ooh_and_sign:
            df_pivot_working_hours_with_sign[column] = 0

    return df_pivot_working_hours_with_sign