def f(n):
    ans = 0
    for i in range(1000):
        ans = ans + 1
    print('number of additions so far: ', ans)
    for i in range(n):
        ans = ans + 1
    print('number of additions so far:', ans)
    for i in range(n):
        for j in range(n):
            ans = ans + 1
            ans = ans + 1
    print('number of additions so far:', ans)
    return ans

# Return decimal string representation of non-negative input i
def intToStr(n):
    digits = '0123456789'
    if n == 0:
        return '0'
    result = ''
    while n > 0:
        result = digits[n%10] + result
        n = n//10
        print(result)
    return result

def matrixMult(m1, m2):
    numRowsM1 = len(m1)
    numRowsM2 = len(m2)
    numColsM2 = len(m2[0])
    result = [[0 for col in range(numColsM2)] for rows in range(numRowsM1)]
    for i in range(numRowsM1):
        for j in range(numColsM2):
            for k in range(numRowsM2):
                result[i][j] = m1[i][k] * m2[k][j]
    return result

def genMatrix(n):
    return [[1 for col in range(n)] for rows in range(n)]
       
import time

# try timeMatrixMult with arguments of, say, 100, 200, 400 to see time growth pattern
def timeMatrixMult(size = 100):
    t1 = time.time()
    m = genMatrix(size)
    print("{}-by-{} matrix created".format(size, size))
    t2 = time.time()
    result = matrixMult(m, m)
    print("matrix multiplication finished")
    t3 = time.time()
    print("create matrix time: ", t2-t1)
    print("multiply matrices time: ", t3-t2)


