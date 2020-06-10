
def readSMSes(fileName):
    inFileStream = open(fileName, encoding = 'utf-8')
    SMSes = []
    for line in inFileStream:
        splitLine = line.split()
        cleanSplitLine = [token.strip('.,!?').lower() for token in splitLine]
        hamOrSpam = cleanSplitLine[0]
        if hamOrSpam not in ['ham', 'spam']:
            print("Found a line not labeled 'ham' or 'spam' ... just skipping it!")
        else: 
            SMSes.append([hamOrSpam, cleanSplitLine[1:]])
    return SMSes

def analyzeSMS(listOfTokens, dictForData):
    for token in listOfTokens:
        if len(token) > 0:
            if token in dictForData:
                dictForData[token] = dictForData[token] + 1
            else:
                dictForData[token] = 1

# use optional argument minLength to print frequency data only for words >= minLength
# E.g., 4 seems a little more informative than 1 for minLength
#
def hamAndSpam(smsFilename, minLength=1):
    listOfSplitSMSes = readSMSes(smsFilename)
    spamDict = {}
    hamDict = {}
    hamCount = 0
    spamCount = 0
    for tagAndSMS in listOfSplitSMSes:
        if tagAndSMS[0] == 'ham':
            hamCount = hamCount + 1
            analyzeSMS(tagAndSMS[1], hamDict)
        else:
            spamCount = spamCount + 1
            analyzeSMS(tagAndSMS[1], spamDict)
    spamValues = spamDict.values()
    spamKeys = spamDict.keys()
    numDiffSpamWords = len(spamKeys)
    totalSpamWords = sum(spamValues)
    spamList = zip(spamValues, spamKeys)
    sortedSpamList = sorted(spamList, key=lambda pair: pair[0], reverse=True)                          
    hamValues = hamDict.values()
    hamKeys = hamDict.keys()
    numDiffHamWords = len(hamKeys)
    totalHamWords = sum(hamValues)
    hamList = zip(hamValues, hamKeys)
    sortedHamList = sorted(hamList, key=lambda pair: pair[0], reverse=True)

    topSpam = [((item[0]/float(totalSpamWords)),item[1]) for item in sortedSpamList if len(item[1]) >= minLength]
    topHam = [((item[0]/float(totalHamWords)),item[1]) for item in sortedHamList if len(item[1]) >= minLength]

    print("Data consists of {} ham and {} spam messages.".format(hamCount, spamCount))
    print()
    print("Average length of a ham message: {:.2f}".format(totalHamWords/hamCount))
    print("Average length of a spam message: {:.2f}".format(totalSpamWords/spamCount))   
    print("Unique spam words: {}, total spam words: {}".format(numDiffSpamWords, totalSpamWords))
    print("Unique ham words: {}, total ham words: {}".format(numDiffHamWords, totalHamWords))
    print()
    print("Most frequent words of at least {} letters (by percentage):".format(minLength))
    print("\nSpam\t\tHam")
    for i in range(min(len(topHam),len(topSpam),30)):
        print("{}\t{:.2f}\t{}\t{:.2f}".format(topSpam[i][1],topSpam[i][0]*100, topHam[i][1],topHam[i][0]*100))
   

