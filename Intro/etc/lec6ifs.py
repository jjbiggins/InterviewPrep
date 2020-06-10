def test1 (input):
    print("At beginning of test1 function ...")
    if input == 1:
        print("Yes, it's 1")
    else:
        print("No, it's not 1")
    print("At end of test1 function ...")
    return

# Understand what's going on in the functions below
# i.e. be careful and precise when you write code :) !

def testyes1(input):
    if (input == 'Si' or 'si' or 'SI'):
        print('Yes :)')
    else:
        print('No :(')
        
def testyes2(input):
    if (input == ('Si' or 'si' or 'SI')):
        print('Yes :)')
    else:
        print('No :(')

def testyes3(input):
    if ((input == 'Si') or (input == 'si') or (input == 'SI')):
        print('Yes :)')
    else:
        print('No :(')

        
# Make sure you can figure out (in your head - without actually executing it) what this prints
# under different inputs.
# E.g. what does ifs(12, 3, 5) print?
#        what does ifs(25, 25, 25) print?
#
def ifs(x, y, z):
    if ((y > z) or (z < x)):
        print("MOT")
        if (x < 10):
            print("HAI")
        elif (z < 10):
            print("BA")
        print("BON")
    else:
        if (x < 20):
            print("NAM")
        else:
            print("SAU")
        print("BAY")
    if ((z-y) > 0):
        print("TAM")


