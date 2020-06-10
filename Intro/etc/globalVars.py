# Here, x is global (since not a parameter of f0 and not assigned to within f0)
# Crashes if x not given a value at top level / in shell before calling f0
def f0():
    print(x + 1)

# Here x is local (since assigned to in f1())
# Why does it crash?
def f1():
    x = x + 1
    print("In f1. x == ", x)

# Here, the 'global x' line makes references to x in f2 global.
# So assignments are to global rather than local value of x
#
def f2():
    global x
    x = x + 1
    print("In f2. x == ", x)

def setX1(value):
    x = value
    print("In setX1, after setting x. x == ", x)    

def setX2(value):
    global x
    print("In setX2, before setting x. x == ", x)
    x = value
    print("In setX2, after setting x. x == ", x)
    
def testGlobals():

    print("In testGlobals. Initially, (global) x == ", x)
    setX1(5)
    print("In testGlobals, after calling setX1, (global) x == ", x)    
    setX2(10)
    print("In testGlobals, after calling setX2, (global) x == ", x)
    
    


