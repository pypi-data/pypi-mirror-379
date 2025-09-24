import pandas as pd

def enriching_time_features(df_meta_with_value, period_freq='M', 
                            schedule_records = None,
                            ooh_values=['OUT OF HOURS', 'POST TRADE', 'closed'],
                            weekend=None, 
                            working_end_time=None, 
                            working_start_time=None,
                            timezone='UTC'):
    
    if weekend == None:
        weekend = 5
    if working_end_time == None:
        working_end_time = "18:00:00"
    if working_start_time == None:
        working_start_time = "08:00:00"

    # manipulate and clean the data

    # print('df_meta_with_value.head(3).time: ', df_meta_with_value.head(3).time)

    df_meta_with_value.time = pd.to_datetime(df_meta_with_value.time).dt.tz_convert(timezone)

    # print('df_meta_with_value.head(3): ', df_meta_with_value.head(3)) # test
    df_meta_with_value = df_meta_with_value.set_index("time") 

    # enrich_time_information
    df_meta_with_value["date"] = df_meta_with_value.index.date
    df_meta_with_value["day_of_month"] = df_meta_with_value.index.day
    df_meta_with_value["time_of_day"] = df_meta_with_value.index.time

    df_meta_with_value['time_of_day_in_float'] = df_meta_with_value.index.hour+df_meta_with_value.index.minute/60+df_meta_with_value.index.second/3600

    df_meta_with_value["weekday"] = df_meta_with_value.index.weekday
    df_meta_with_value["day_name"] = df_meta_with_value.index.day_name()
    df_meta_with_value["day_code"] = df_meta_with_value["day_name"].str[0]
    df_meta_with_value["month"] = df_meta_with_value.index.month
    df_meta_with_value["month_name"] = df_meta_with_value.index.month_name() #new change/implementation -RP

    # print('schedule_records: ', schedule_records)

    if schedule_records is not None:

        df_meta_with_value["out_of_hours"] = False

        for schedule_record in schedule_records:
            # print('schedule_record: ', schedule_record)
            if schedule_record['name'] in ooh_values:
                df_meta_with_value["out_of_hours"] |= (df_meta_with_value['day_name'] == schedule_record['day']) & \
                                                (df_meta_with_value["time_of_day"] >= schedule_record['start_time']) & \
                                                (df_meta_with_value["time_of_day"] < schedule_record['end_time'])
                
                # print('ooh exist:', sr_ooh_record.unique())
                ## For out of hour - POST TRADE, OUT OF HOUR
                ## For In Hour - PRE TRADE, TRADE

                # If out of hour - then run the below files,  checkpoint - POST TRADE & OUT OF HOUR
                # if !out of hour - checkpoint - POST TRADE | OUT OF HOUR, run different file
    else:
        df_meta_with_value["out_of_hours"] = df_meta_with_value['weekday'].ge(weekend) | \
                                                (df_meta_with_value["time_of_day"] > pd.to_datetime(working_end_time).time()) | \
                                                (df_meta_with_value["time_of_day"] < pd.to_datetime(working_start_time).time())
    
    df_meta_with_value["period"] = df_meta_with_value.index.tz_localize(None).to_period(freq=period_freq)
    
    return df_meta_with_value