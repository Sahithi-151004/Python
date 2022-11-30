import calendar

a = int(input(" Enter the year that you want to check: "))

num = calendar.isleap(a)

if num == True:

    print("The year entered %s is a Leap Year" %a)

else:
    print("The year entered %s is not a Leap Year" %a)
