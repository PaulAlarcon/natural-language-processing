def writeToFile(url, container):
    bt = open(url, "w")
    for string in container:
        bt.write(string)
    bt.close()

def padSentence():
    paddingSentence('brown-train')  # padding the brown-train file
    paddingSentence('learner-test')  # padding the learner-test file
    paddingSentence('brown-test')  # padding the brown-test file

def paddingSentence(url):
    # constant to append and prepend
    prepend = '<s>'
    append = '</s>'

    # store all the strings from reading the files
    container = []

    # reading from the file
    openFile = open(url + '.txt', 'r')
    openRead = openFile.readlines()

    for currentLine in openRead:
        # print(currentLine)
        currentLine = currentLine.lower()  # lowecase everything
        lastIndex = len(currentLine) - 1
        currentLine = currentLine[:lastIndex] + " " + \
            append + " " + currentLine[lastIndex:]
        container.append(prepend + " " + currentLine)
    openFile.close()
    
    writeToFile(url+"-after.txt", container)

def createDictionaryUnigram():
    d = dict()  # my dictionary

    openFile = open('brown-train-after.txt', 'r')
    openRead = openFile.readlines()

    for currentLine in openRead:
        for oneString in currentLine.split(" "):
            if oneString in d:
                d[oneString] += 1
            else:
                d[oneString] = 1

    f = open("dictUnigram.txt", "w")
    f.write(str(d))
    f.close

    return d

def createDictionaryBigram():
    d = dict()  # my dictionary

    openFile = open('brown-train-after.txt', 'r')
    openRead = openFile.readlines()

    for currentLine in openRead:
        split = currentLine.split(" ")

        for index in range(len(split) - 1):
            combinedString = split[index] + " " + split[index+1]
            if combinedString in d:
                d[combinedString] += 1
            else:
                d[combinedString] = 1

    f = open("dictBigram.txt", "w")
    f.write(str(d))
    f.close

    return d

def replaceOccuringOnce(d, url):
    # REPLACE ALL WORD OCCURING IN TRAINING DATA ONCE WITH THE TOKEN UNK
    # Reading from the file
    openFile = open(url + '.txt', 'r')
    openRead = openFile.readlines()

    container = []

    # REPLACE THE WORD WITH UNKNOWN
    for currentLine in openRead:
        # print(currentLine)
        txt = ""
        currentLine = currentLine.lower()  # lowecase everything
        for oneString in currentLine.split(" "):
            if d.get(oneString) == 1:
                txt = txt + " <unk>"
            else:
                txt = txt + " " + oneString
        container.append(txt)
    openFile.close()

    writeToFile(url+"-replaced-unk.txt", container)

def replaceNotOccuring(d, url):
    # REPLACE ALL WORD OCCURING IN TRAINING DATA ONCE WITH THE TOKEN UNK
    # Reading from the file
    openFile = open(url + '.txt', 'r')
    openRead = openFile.readlines()

    container = []

    # REPLACE THE WORD WITH UNKNOWN
    for currentLine in openRead:
        # print(currentLine)
        txt = ""
        currentLine = currentLine.lower()  # lowecase everything
        for key in currentLine.split(" "):
            if key not in d.keys():
                txt = txt + " <unk>"
            else:
                # print("appear " + key)
                txt = txt + " " + key
        container.append(txt)
    openFile.close()

    writeToFile(url+"-replaced-unk.txt", container)

def replaceOccuring():
    d = createDictionaryUnigram()  # my dictionary
    print('--Replacing the word occured once in brown-train file with unk--')
    replaceOccuringOnce(d, 'brown-train-after')

    print('--Replacing the word not appeared in brown-test file with unk--')
    replaceNotOccuring(d, 'brown-test-after')

    print('--Replacing the word not appeared in brown-test file with unk--')
    replaceNotOccuring(d, 'learner-test-after')