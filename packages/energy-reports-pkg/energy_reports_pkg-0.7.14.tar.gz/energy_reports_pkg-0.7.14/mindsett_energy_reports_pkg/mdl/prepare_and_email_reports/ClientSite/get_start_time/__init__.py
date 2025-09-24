
def get_start_time(self):

        period_range = self.get_period_range()
        start_time = period_range[-(self.period_offset_previous+1)].start_time # start time of the (previous) period to be compared
        return start_time