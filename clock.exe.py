startTime = int(input("What Is The Start Time? "))
alarmDelay = int(input("Wait How Long? "))
alarmTime = startTime + alarmDelay
daysLater = alarmTime //24
hourOfDay = (alarmTime % 24) 
print("The Alarm Will Go Off " + str(daysLater) + "days and at " +  str(hourOfDay) + "00" )
