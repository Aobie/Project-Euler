#Euler19
import time

startday = 2
Days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

Months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
          'August', 'September', 'October', 'November', 'December']
          
stndays = {'January':31, 'February':28, 'March':31, 'April':30, 'May':31, 'June':30, 'July':31,
       'August':31, 'September':30, 'October':31, 'November':30, 'December':31}
       	
#How many times has Day fallen on the first of the month in the given Century
def first_day_count_cent(Day, Startyear, Startday):
    if Startday == Day:
        daycount = 1
    else:
        daycount = 0
    testday = Days.index(Startday)
    for year in range(Startyear, Startyear + 100):
        if year % 4 == 0 and (year % 100 or year % 400 == 0):
            leap = True
        else:
            leap = False
        for month in Months:
            #print(month, "-------------")
            #print("Test Day: ", Days[testday])
            if testday == Days.index(Day):
                daycount += 1
                #print(month, ": ", Day)
            if month == 'February' and leap == True:
                dayinc = 29
            else:
                dayinc = stndays[month]
            #print(dayinc)
            dayinc %= 7
            if (dayinc + testday) >= 7:
                testday = (testday + dayinc) - 7
            else:
                testday += dayinc
            
    return daycount
    


if __name__ == "__main__":
    print("Problem 19")
    print("How many Sundays fell on the first of the month during the 20th Cent?")
    t1 = time.time()
    answer = first_day_count_cent('Sunday', 1901, 'Tuesday')
    t2 = time.time()
    print((t2-t1)*1000.0, " ms")
    print(answer)
