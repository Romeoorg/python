# # Date Time Function

 

# import datetime

# now = datetime.datetime.now()

# print("Current date and time: ")

# print(now)

# print(now.strftime("%Y-%m-%d %H:%M:%S"))







# Date and Time Module

# Dispalying only the date

 

# import datetime

# today = datetime.date.today()

# new_year = datetime.date(2024, 5, 13)

# print(new_year)

 

# Printing from start date - end date

#Function: Day Delta

 

# import datetime

# day_delta = datetime.timedelta(days = 1) # days = 1 refers to the days you want to display at a time. Aka Steps like in slicing

# # print(day_delta)

 

# start_date = datetime.date.today()

# # print(start_date)

 

# end_date = start_date + 5*day_delta

# # print(end_date)

 

# for i in range((end_date - start_date).days):

#     print((start_date + i*day_delta))

# import datetime
# #print nexr five days

# five_days = datetime.date.today()

# print(five_days)

# while five_days == datetime.date.today():
#      print(five_days)
#      datetime.datetime.today=datetime.datetime.today+1



#5 days before stock
# import datetime
# day_delta = datetime.timedelta(days = 1)

# current_date = datetime.date.today()
# prior_date = current_date - 5*day_delta

# print(f"Current date {current_date}")

# print(f"5 days before {prior_date}")


# UNIX a person of encoded information OR time stamp
# convert a unix time stamp into a readable date

# import datetime
# UNIz = datetime.date.fromtimestamp
# print(UNIz)

# print(UNIz.strftime(UNIz))


#write a code to get the current time in milliseconds

# import time
# Milliseconds_time = int (round(time.time()*1000))

# print(Milliseconds_time)

# find the date of the first monday of a given week
#struct coverts given time in seconds,this is the ty
# import time

# print(time.asctime(time.strptime("2024 10 2","%Y %W %w")))

# # to select all the sundays in a specofied year/2024

from datetime import date,time,timedelta

# def all_sundays(year):
#     #set datetime to jan/startdatetime  = jan 1
#     dt = date(year,1,1)
   

#     #Move dt to first sun of the year

#     dt = dt + timedelta(days = 6-dt.weekday())

#     #Iterate through all sundays of the year
#     while dt.year == year:
#         #yield the current date as results
#         yield dt

#         #move to the next sunday by adding 7 days
#         dt= dt + timedelta(days= 7)
 
# for s in all_sundays(2021):
#         print(s)       

#Add year to a giving date and display the date,2021,2020,2022 and 2023
#leap year

# import datetime
# from datetime import date


# def add_years(d, years):
#     try:
#         return d.replace(year = d.year + years)
#     except ValueError:
#         return d + (date(d.year + years, 1, 1))
    
# #adding -1 year
# print(add_years(datetime.date(2024,1,1),-4))

# #adding 0 year 
# print(add_years(datetime.date(2020,1,1),-0))

# #adding 1 year 
# print(add_years(datetime.date(2020,1,1),1))




#Previous 5 years

# import datetime
# from datetime import date


# def add_years(d, years):
#     try:
#         return d.replace(year = d.year + years)
#     except ValueError:
#         return d + (date(d.year + years, 1, 1))

# print(add_years(datetime.date(2020,1,1),1))
# for in range(0,5):
#     print()



#the number of days betwwen two dates
# from datetime import date

# def difference_days(date_1,date_2):
#     a=date_1
#     b=date_2
#     return (b-a).days
 
 #print()
# print(f"difference in days 😅  ({difference_days((date(2020,10,10)), date(2024,10,12))})")

# date_4=date(2020,10,10)
# date_3 = date(2024,10,12)
# x = date_4-date_3

# print(x)

#c time takes a single argument and returns it as a string , that represent local time
#used two normal brackets
# import time
# print((time.ctime()))


 #Pendulum time manipulation library,provies a cleaner more readable or concise interface
# import pendulum 
# from datetime import date
# #get the current date and time

# current_date_time = pendulum.now()
# print(f"Current time {(current_date_time.strftime("%Y-%m-%d %H:%M:%S"))}")

#write the code to format the current date and time,days hours minutes and seconds


#Write a code that adds 5 seconds to current time time

import datetime

x = datetime.datetime.now()
y = x + datetime.timedelta(0,5)

print(f"Current time {(x)}")
print(f"added time {(y)}")

 