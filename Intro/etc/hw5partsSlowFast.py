
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

def getHamOrSpamWordListSlow(smses, hamOrSpam):
    wordList = []
    for sms in smses:
        if sms[0] == hamOrSpam:
            for word in sms[1]:
                wordList = wordList + [word]
    return wordList

def getHamOrSpamWordListFast(smses, hamOrSpam):
    wordList = []
    for sms in smses:
        if sms[0] == hamOrSpam:
            wordList.extend(sms[1])
    return wordList

def processWordListSlow(wordList):
    counts = []
    doneList = []
    for word in wordList:
        if word not in doneList:
            counts.append(wordList.count(word))
            doneList.append(word)
    return counts

def processWordListFast(wordList):
    d = {}
    for word in wordList:
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1
    counts = list(d.values()) # not exactly the same as counts in processWordListSlow but same amount of useful infomation
    return counts

import time

# use 'slow', 'alittlefaster', 'fast' for speed argument
# do
# test(smsType='spam', speed='slow')
# test(smsType='spam', speed='alittlefaster')
# test(smsType='spam', speed='fast')
#
# Do 'ham' as well - the first might takes a couple of minutes on a basic computer
# test(smsType='ham', speed='slow')
# test(smsType='ham', speed='alittlefaster')
# test(smsType='ham', speed='fast')
#
# NOTE: assumes you have file SMSSpamCollection.txt in the same folder
#
def test(smsType='spam', speed='slow'):
    time1 = time.time()
    s = readSMSes('SMSSpamCollection.txt')
    time2 = time.time()
    print('done reading file')
    if speed == 'slow':
        hl = getHamOrSpamWordListSlow(s, smsType)
    else:
        hl = getHamOrSpamWordListFast(s, smsType)
    time3 = time.time()
    print('created {} word list'.format(smsType))
    if speed != 'fast':
        cl = processWordListSlow(hl) 
    else:
        cl = processWordListFast(hl)
    print(len(cl))
    time4 = time.time()
    print("read file time: ", time2-time1)
    print("create word list time: ", time3 - time2)
    print("calculate counts time: ", time4 - time3)
    
