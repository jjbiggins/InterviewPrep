# Examples from Jan. 27 lecture.
# Very important to understand #1 and #3.
# #2 is less important for now.  Good programming style/design often
# avoid situations like those in #2.

# 
#####
#1. simple local variable example

def f(x):
    y = 1
    x = x + y
    print("x (as seen inside function f) has value: {}".format(x))
    return x

# demo in interpreter via:
# x = 3
# y = 2
# z = f(x)
# z
# y
# x


#####
# 2. special small examples:

# f1: accessing global/non-local value (if a variable is mentioned in a function but *not* assigned-to,
#      then it references the global value
# f1() crashes is no global x value has been set
# f1() prints global x value if one has been set
def f1():
    print(x+1)

# f2: call to f1, f1 still accesses "top level"/global x, not f2's local x!
def f2():
    x = 1
    print(x)
    f1()

# f3: oddly demonstrates python rule of: if you assign to variable in function body
# that variable is local.  This function does *not* first access non-local/global x, then
# assign to local (or global x). Instead it ??? (try it)
def f3():
    print(x)
    x = 1

#####
# 3. It is important that you understand this longer example, and why all the
# variables have the values they do when printed out.
# Draw stack frames by hand to help understand it!
# 

def fn3(x):
    print("Entered fn3. Local x = ", x, "non-local z = ", z)
    y = 3 * x + 3 + z
    x = y + 3
    print("Leaving fn3. Local x =", x, "y =", y)
    return x
 
    
def fn2(x):
    print("Entered fn2. Local x = ", x)
    z = 4
    y = 2 * x + z + 2
    x = fn3(y) + 2
    print("Leaving fn2. Local x = ", x, "y =", y, "z = ", z ) 
    return x

def fn1(x):
    print("Entered fn1. Local x = ", x)
    y = x+1
    x = fn2(y)+1
    print("Leaving fn1. Local x = ", x, "y =", y)
    return x

# execute of the following in Python. But also do "by hand" on paper,
# drawing stack frames  to keep track of different variables/values 
# >>> x = 0
# >>> z = 5
# >>> fn1(x+1)
# >>> print(x)
# >>> print(z)


def add1a(number):
    result = number + 1
    print(result)

def add1b(number):
    result = number + 1
    return(result)

