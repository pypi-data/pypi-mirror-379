

def generate_day_code_list(datetime_list):
    
    previous_day_month = None
    previous_day_year = None
    day_code_list = []

    len_dates = len(datetime_list)

    for item in datetime_list:
        weekday_str = item.day_name()[0]

        # handle the case that for monthly reports, the day numbers will be very close to each other
        if (len_dates < 20) or (weekday_str=='M'): 
            day_str = "\n"+str(item.day)
        else:
            day_str = "\n "

        # the month and year are only added when it starts or changes

        if item.month == previous_day_month:
            month_str = ""
        else:
            month_str = " "+str(item.strftime("%b"))
        previous_day_month = item.month

        if item.year == previous_day_year:
            year_str = ''
        else:
            year_str = " "+str(item.year)
        previous_day_year = item.year

        day_code = weekday_str+day_str+'\n'+month_str+year_str

        day_code_list.append(day_code)
        
    return day_code_list