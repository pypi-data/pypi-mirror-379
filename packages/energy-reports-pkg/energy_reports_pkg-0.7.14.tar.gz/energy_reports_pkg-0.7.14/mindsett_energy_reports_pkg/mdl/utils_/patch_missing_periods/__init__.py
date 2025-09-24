
import pandas as pd

def patch_missing_periods(df_source, start_time, end_time, 
                          time_col='time',
                          value_col='kwh',
                          period_freq='W',
                          timezone='UTC'):
    
    # print('start_time, end_time:', start_time, end_time)

    end_time_inclusive = end_time - pd.Timedelta(microseconds=1)

    # print('df_source: ', df_source.sort_values(by=['time'], ascending=False).head())
    actual_periods_ls = pd.to_datetime(df_source.time, utc=True).dt.tz_convert(tz=timezone).dt.tz_localize(None).dt.to_period(freq=period_freq).unique()
    expect_periods_ls = pd.period_range(start=start_time, end=end_time_inclusive, freq=period_freq)

    # print('actual_periods_ls: ', actual_periods_ls)
    # print('expect_periods_ls: ', expect_periods_ls)

    for period_obj in expect_periods_ls:
        if period_obj not in actual_periods_ls:
            
            print(f'There is no data in period {period_obj}. A placeholder with zero consumption has been added!')
            print('start_time', period_obj.start_time)
            df_placeholder = df_source.head(1)
            with pd.option_context('mode.chained_assignment', None):
                df_placeholder[value_col] = 0
                df_placeholder[time_col] = pd.Timestamp(period_obj.start_time, tz=timezone)
                df_source = pd.concat([df_source, df_placeholder], ignore_index=True)
                df_source.loc[:, time_col] = pd.to_datetime(df_source[time_col], utc=True)
    
    # print('df_source: ', df_source.head())
    return df_source