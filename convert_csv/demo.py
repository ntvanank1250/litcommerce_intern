from datetime import datetime

# date_time_str = '18/09/19 01:55'
date_time_str = '10/1/2019 6:47'


date_time_obj = datetime.strptime(date_time_str, '%d/%m/%Y %H:%M')


print ("The type of the date is now",  type(date_time_obj))
print ("The date is", date_time_obj)