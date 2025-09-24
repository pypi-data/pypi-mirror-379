

def get_end_time(self):

    period_range = self.get_period_range()
    # end_time = period_range.max().start_time # end time of the most recent finished period
    end_time = period_range[-(self.period_offset)].start_time # end time of the offset period
    return end_time