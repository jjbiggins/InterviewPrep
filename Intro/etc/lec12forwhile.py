# ???
# To convert foo to use of while instead of for, you don't need to understand 
#  what the function actually computes ...
def foo(l, a, b, x, y):
    z = 23 * b - x
    q = list(range(y))
    for bbb in l:
        
        r = a - q[0] + l[1] - 14 + bbb
        r2 = x + y / r
        r = r2 + r + r
        
    return r / 3.0

def foo2(l, a, b, x, y):
    z = 23 * b - x
    q = list(range(y))
    index = 0
    while (index < len(l)):
        bbb = l[index]
        
        r = a - q[0] + l[1] - 14 + bbb
        r2 = x + y / r
        r = r2 + r + r

        index = index + 1
        
    return r / 3.0

