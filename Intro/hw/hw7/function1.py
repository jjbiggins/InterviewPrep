# Assumes n is a non-negative integer
def function1(n):
    ans = 0
    for i in range(n):
        xyz = i + (i * 1.1) + n/2.5
        abc = xyz + i/2 + (3*i)%(i+1)
        j = n*n
        while j > 1:
            bde = xyz + abc + i + j
            j = j - 1
            ans = (ans + bde) % (1100000)
    return ans



