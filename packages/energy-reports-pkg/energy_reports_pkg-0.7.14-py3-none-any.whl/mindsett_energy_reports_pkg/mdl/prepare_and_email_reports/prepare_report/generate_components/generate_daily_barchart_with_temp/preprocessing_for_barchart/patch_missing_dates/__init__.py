import pandas as pd

def patch_missing_dates(df_pivot_working_hours, period_current):

    start_date = period_current.start_time.date()
    end_date = period_current.end_time.date()

    # firstly ensuring that the start and finish date are not missing
    if start_date not in df_pivot_working_hours.index:
        df_pivot_working_hours.loc[start_date] = 0

    if end_date not in df_pivot_working_hours.index:
        df_pivot_working_hours.loc[end_date] = 0

    # convert the date index to full datetime, so it can be used to adjust frequency
    df_pivot_working_hours.index = pd.to_datetime(df_pivot_working_hours.index)
    df_pivot_working_hours_patched = df_pivot_working_hours.asfreq('1D', fill_value=0).fillna(0)

    # convert the full datetime frequency to date following the original format
    df_pivot_working_hours_patched.index = df_pivot_working_hours_patched.index.date

    return df_pivot_working_hours_patched



    
    

