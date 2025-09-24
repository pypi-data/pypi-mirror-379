import pandas as pd

def generate_time_partition_list(time_range, freq='1D'):
    
    start_time_str = time_range[0]
    end_time_str = time_range[1]
    
    time_list = pd.date_range(start=start_time_str, end=end_time_str, freq=freq).to_list()

    time_str_list = [time.strftime("%Y-%m-%d %X%z") for time in time_list]

    time_range_list = list(zip(time_str_list[:-1], time_str_list[1:]))
    
    return time_range_list