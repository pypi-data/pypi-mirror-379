from .patch_missing_dates import patch_missing_dates
from .patch_missing_columns_for_ooh_and_sign import patch_missing_columns_for_ooh_and_sign
from .groupby_date_and_ooh_current_period import groupby_date_and_ooh_current_period

# from .groupby_date_and_ooh_current_period import groupby_date_and_ooh_current_period

from cache_return import cache_return


@cache_return
def preprocessing_for_barchart(df_meta_with_value_bld):
    
    # main operation
    df_pivot_working_hours_with_sign_sorted, period_current = groupby_date_and_ooh_current_period(df_meta_with_value_bld)

    # patch the missing ooh columns and period index
    df_pivot_working_hours_with_sign_sorted = patch_missing_columns_for_ooh_and_sign(df_pivot_working_hours_with_sign_sorted)
    df_pivot_working_hours_with_sign_sorted = patch_missing_dates(df_pivot_working_hours_with_sign_sorted, period_current)

    return df_pivot_working_hours_with_sign_sorted, period_current
    # pass