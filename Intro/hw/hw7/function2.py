
# Assumes L is a non-empty list of non-negative integers, x is an integer
def function2(L, x):
    ans = 0
    index = len(L)
    while (index > 0):
        i = 0
        while i < 1000000:
            i = i + 1
        ans = ans + L[index - 1]
        index = index // 2
    
    if (x == L[-1]):
        return ans
    else:
        for i in range(len(L)):
            ans = ans + 1
    return ans


