import hashlib

def readPeopleInfoFile(filename):
    global peopleDict
    peopleDict = {}
    file = open(filename, 'r')
    for line in file:
        print(line)
        lineAsList = line.split()
        print(lineAsList)
        key = lineAsList[0]
        subDict = {}
        subDict['birthyear'] = lineAsList[1]
        subDict['favcolor'] = lineAsList[2]
        subDict['weight'] = lineAsList[3]
        subSubDict = {}
        subSubDict['city'] = lineAsList[4]
        subSubDict['country'] = lineAsList[5]
        subDict['home'] = subSubDict
        peopleDict[key] = subDict
    return

def printAllHomeCities():
    for name in peopleDict:
        peopleInfo = peopleDict[name]
        homeInfo = peopleInfo['home']
        city = homeInfo['city']
        print(city)
        #print(peopleDict[name]['home']['city'])
        

# for fun

def hashPassword(password):
    userPassword = password.encode('utf-8')
    hashResult = hashlib.sha1(userPassword)
    hexResult = hashResult.hexdigest()
    return(hexResult)

def getMyData():
    global peopleDict
    name = input("Enter your name: ")
    if (name not in peopleDict):
        print("Sorry, there is no entry for you in our database.")
        return 
  
    record = peopleDict[name]
    if  ('password' not in record):
        print("You need to set a password.")
        password = input("Please enter a new password: ")
        record['password'] = hashPassword(password)
        print("Password successfully saved.")
        print

    numberOfAttempts = 0
    loginSuccessful = False
    while (loginSuccessful == False and numberOfAttempts < 3):
        enteredPassword = input("Enter your password: ")
        hashValue = hashPassword(enteredPassword)
        print(hashValue)
        if (hashValue == record['password']):
            loginSuccessful = True
        else:
            print("Sorry, the password you entered is not correct.")
        numberOfAttempts = numberOfAttempts + 1
        
    if loginSuccessful == False:
        print("Please try again later.")
    else:
        print("Your information is: ", record)
        print()





    
