def inBoth(string1, string2):
    for char in string1:
        if char in string2:
            print(char)
    return

# code from example in textbook's Chapter 8 "Debugging" section
# See text for discussion of correctness ..
#
def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    i = 0
    j = len(word2)

    while j > 0:
        # Use print line below to help debug ...
        # print("i = ", i, "j = ", j)
        if word1[i] != word2[j]:
            return False
        i = i + 1
        j = j - 1

    return True

def traverseList(l):
    for number in l:
        if number < 0:
            print("negative")
        else:
            print("not negative")
            

    
