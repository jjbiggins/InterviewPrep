# suppose we want pattern
#
# printStuff(3,6) to yield
#
# 3
# ***
# **
# *
# 4
# ****
# ***
# **
# *
#...
# 6
# ******
# *****
# ****
# ***
# **
# *
#
# Start with "outline":
#
#  def printStuff(low, high):
#       # initialize counter
#       # while (condition involving counter):
#       # print correct number
#       # print a suitable "pyramid" of stars on several lines
#       # update counter
#
# and refine/add code a bit at a time.  

def printStarPyramid(size):
    current = size
    while ( current > 0):
            print(current * '*')
            current = current - 1
    return

def printStuff(low, high):
    current = low
    while (current <= high):
        print(current)
        printStarPyramid(current)
        current = current + 1      
    return
