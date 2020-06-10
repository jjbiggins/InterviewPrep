class Time:
    '''class for representing time (in seconds from 0 to 23 hours, 59 minutes, 59 seconds.)'''

    def __init__(self,  hour = 0, minutes = 0, seconds = 0):
        self.hour = hour
        self.minutes = minutes
        self.seconds = seconds
    
    def __repr__(self):
        return "Time({}, {}, {})".format(self.hour, self.minutes, self.seconds)

    def __str__(self):
        ampm = "AM" if self.hour <12 else "PM"
        return "{:02d}:{:02d}:{:02d} {}".format(self.hour%12,self.minutes,self.seconds, ampm)

    def __add__(self, seconds):
        return self.later(seconds)
    
    def __radd__(self, seconds):
        return self.later(seconds)

    def increment(self, seconds):
        '''time.increment(seconds) -> None. Modify time to be seconds later than time's current value'''
        newSeconds = self.seconds + seconds
        minutesCarried = newSeconds // 60
        self.seconds = newSeconds % 60

        newMinutes = self.minutes + minutesCarried
        hoursCarried = newMinutes // 60
        self.minutes = newMinutes % 60

        newHour = (self.hour + hoursCarried) % 24
        self.hour = newHour
            
    def later(self, seconds):
        '''time.later(seconds) -> Time. return a new Time object that is seconds later than time's time'''
        laterTime = Time(self.hour, self.minutes, self.seconds)
        laterTime.increment(seconds)
        return laterTime
    
def testTime():
    t1 = Time(1, 23, 59)
    print(t1)

    t1.increment(5)
    print(t1)
    
    t1.increment(23*3600 + 3599)
    print(t1)
       
def testTime2():
    t2 = Time(11, 59, 59)
    print('t2 is: ', t2)
    
    t3 = t2.later(2)
    print('t3 is: ', t3)
    print('t2 is: ', t2)

def testTime3():
    t2 = Time(11, 59, 59)
    print(t2 + 2)
    print(3 + t2)
    

    
