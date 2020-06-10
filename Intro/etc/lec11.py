def generatePairs(list1, list2):
    result = []
    for item1 in list1:
        print(result)
        for item2 in list2:
            #result = result + [ [item1, item2] ]
            result.append([item1,item2])
    return result

def sublistSums(listOfLists):
    result = []
    for sublist in listOfLists:
        # add up numbers in sublist and append sum to result
        sum = 0
        for number in sublist:
            sum = sum + number
        #  result = result + [ sum ]
        result.append(sum)
    return result

