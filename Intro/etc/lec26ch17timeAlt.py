# same as ch17time.py EXCEPT that uses only one attribute - seconds - to represent time internally.
# Interface - methods available to users of the class - remains exactly the same. Users don't
# need to know about attributes used to represent things internally.

class Time:
    '''class for representing time (in seconds from 0 to 23 hours, 59 minutes, 59 seconds.)'''

    def __init__(self,  hour = 0, minutes = 0, seconds = 0):
        self.seconds = Time.hmsToSecs(hour, minutes, seconds)

    def __repr__(self):
        (h,m,s) = Time.secsToHMS(self.seconds)
        return "Time({}, {}, {})".format(h,m,s)

    def __str__(self):
        (h,m,s) = Time.secsToHMS(self.seconds)
        ampm = "AM" if h <12 else "PM"
        return "{:02d}:{:02d}:{:02d} {}".format(h%12,m,s, ampm)
    
    def hmsToSecs(h,m,s):
        return (h*3600) + (m*60) + s

    def secsToHMS(secs):
        h = secs // 3600
        remSecs = secs - (h*3600)
        m = remSecs // 60
        s = remSecs - (m * 60)
        return(h,m,s)

    def __add__(self, seconds):
        return self.later(seconds)

    def __radd__(self, seconds):
         return self.later(seconds)
        
    def increment(self, seconds):
        '''time.increment(seconds) -> None. Modify time to be seconds later than time's current value'''
        newSeconds = self.seconds + seconds
        newSeconds = newSeconds % (24*3600)
        self.seconds = newSeconds

    def later(self, seconds):
        '''time.later(seconds) -> Time. return a new Time object that is seconds later than time's time'''
        (h,m,s) = Time.secsToHMS(self.seconds)
        laterTime = Time(h,m,s)
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
