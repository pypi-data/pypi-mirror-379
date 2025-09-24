import pandas as pd

def get_period_range(self):

    reference_time = pd.Timestamp.now(tz=self.timezone)  
    period_range = pd.period_range(end=reference_time, freq=self.period_freq, periods=self.period_count+self.period_offset)

    return period_range