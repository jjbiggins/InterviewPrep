# ch16time.py re-done in recommended object-oriented style (of Ch 17)

class Time:
    '''class for representing time.  Use attributes .hour, .minutes, .seconds'''

    def __init__(self,  hour = 0, minutes = 0, seconds = 0):
        self.hour = hour
        self.minutes = minutes
        self.seconds = seconds

    def __repr__(self):
        ampm = "AM" if self.hour <12 else "PM"
        return "{:02d}:{:02d}:{:02d} {}".format(self.hour%12,self.minutes,self.seconds, ampm)
    
    def print(self):
        ampm = "AM" if self.hour <12 else "PM"
        print("{:02d}:{:02d}:{:02d} {}".format(self.hour%12,self.minutes,self.seconds, ampm))

    # modify the given object to be a time later by given seconds       
    def increment(self, seconds):
        newSeconds = self.seconds + seconds
        minutesCarried = newSeconds // 60
        self.seconds = newSeconds % 60
    
        newMinutes = self.minutes + minutesCarried
        hoursCarried = newMinutes // 60
        self.minutes = newMinutes % 60

        newHour = (self.hour + hoursCarried) % 24
        self.hour = newHour

    # return new Time object that is later than given Time object by given seconds
    def later(self, seconds):
        laterTime = Time()
        newSeconds = self.seconds + seconds
        minutesCarried = newSeconds // 60
        laterTime.seconds = newSeconds % 60
    
        newMinutes = self.minutes + minutesCarried
        hoursCarried = newMinutes // 60
        laterTime.minutes = newMinutes % 60

        newHour = (self.hour + hoursCarried) % 24
        laterTime.hour = newHour
        
        return laterTime
    
def testTime():
    t1 = Time(1, 23, 59)
    t1.print()

    t1.increment(5)
    t1.print()
    
    t1.increment(23*3600 + 3599)
    t1.print()

def testTime2():
    t2 = Time(23, 59, 59)
    print('t2 is: ', end = '')
    t2.print()
    t3 = t2.later(2)
    print('t3 is: ', end='')
    t3.print()
    print('t2 is: ', end= '')
    t2.print()
       
def testTime3():
    
    t2 = Time(23, 59, 59)
    print('t2 is: ', t2)
    
    t3 = t2.later(2)
    print('t3 is: ', t3)
    print('t2 is: ', t2)

    

    
