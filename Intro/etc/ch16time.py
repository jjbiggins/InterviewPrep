# A simple Time class done in the not-really-object-oriented style of Ch 15 and 16.
# See ch17time.py for alternative object-oriented approach

class Time:
    '''class for representing time.  Use attributes .hour, .minutes, .seconds'''

def makeTime(hour, minutes, seconds):
    time = Time()
    time.hour = hour
    time.minutes = minutes
    time.seconds = seconds
    return time

def printTimeOrig(time):
    print("{:02d}:{:02d}:{:02d}".format(time.hour,time.minutes,time.seconds))

def printTime(time):
    ampm = "AM" if time.hour <12 else "PM"
    print("{:02d}:{:02d}:{:02d} {}".format(time.hour%12,time.minutes,time.seconds, ampm))

def incrementTime(time, seconds):
    newSeconds = time.seconds + seconds
    minutesCarried = newSeconds // 60
    time.seconds = newSeconds % 60
    
    newMinutes = time.minutes + minutesCarried
    hoursCarried = newMinutes // 60
    time.minutes = newMinutes % 60

    newHour = (time.hour + hoursCarried) % 24
    time.hour = newHour

def testTime():
    t1 = Time()
    t1.hour = 1
    t1.minutes = 23
    t1.seconds = 59
    printTime(t1)

    incrementTime(t1, 5)
    printTime(t1)

    incrementTime(t1, 23*3600 + 3599)
    printTime(t1)

def laterTime(time, seconds):

    laterTime = Time()
    
    newSeconds = time.seconds + seconds
    minutesCarried = newSeconds // 60
    laterTime.seconds = newSeconds % 60

    newMinutes = time.minutes + minutesCarried
    hoursCarried = newMinutes // 60
    laterTime.minutes = newMinutes % 60

    newHour = (time.hour + hoursCarried) % 24
    laterTime.hour = newHour

    return laterTime
    
def testTime2():
    t2 = makeTime(23, 59, 59)
    print('t2 is: ', end = '')
    printTime(t2)
    t3 = laterTime(t2, 2)
    print('t3 is: ', end='')
    printTime(t3)
    print('t2 is: ', end= '')
    printTime(t2)

    

    
