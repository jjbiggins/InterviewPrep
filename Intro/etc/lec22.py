def foo(a, b=0, c=True):
    if c == True:
        return a + b
    else:
        return a - b


# BUT BE CAREFUL!
def bar(num, numList = [100, -100]):
    if num > 0:
        numList[0] = numList[0] + num
    else:
        numList[1] = numList[1] + num       
    return numList

# Simple clear list comprehensions
#
[i * i for i in range(5)]
[s.lower() for s in ["Hi", "Bye"]]
[num for num in [1, -2, 3, -4, 5] if num > 0]


# List comprehensions make it possible to write very concise code. BUT I don't write
# ones like these matrixMult versions.  I think they are too hard to read and debug.
# I use comprehensions only for simple things like those above.
#
M1 = [[1,2,3], [3,4,5]]
M2 = [[5, 10, 20], [100, 200, 1000]]

def matrixMult(A, B):
    return [ [sum([ A[i][j] * B[j][k] for j in range(len(B))]) for k in range(len(B[0])) ] for i in range(len(A))]

def matrixMult2(A, B):
    # Multiply row by (transposed w/zip) col
    return([[ sum([ a*b for (a,b) in zip(row,col) ]) for col in zip(*B) ] for row in A ])
