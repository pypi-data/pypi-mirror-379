

def get_start_time_co2_barchart(self):

    period_range = self.get_period_range()
    start_time_co2_barchart = period_range.min().start_time # start time of the first bar in the co2 barchart
    return start_time_co2_barchart