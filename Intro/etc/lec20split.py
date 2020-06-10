
def readAndSplitLines(inFilename):
    inStream = open(inFilename, encoding = 'utf-8')
    lineCount = 0
    for line in inStream:
        lineAsList = line.split()
        print("File line number {}:".format(lineCount))       
        print(line)
        print(lineAsList)
        print(20*'*')
        lineCount = lineCount + 1
            
        
