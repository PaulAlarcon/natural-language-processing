def writeToFile(url, container):
    bt = open(url, 'w')
    for string in container:
        bt.write(string)
    bt.close()

# padding sentences #

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
        currentLine = currentLine.lower()  # lowecase everything
        lastIndex = len(currentLine) - 1
        currentLine = currentLine[:lastIndex] + ' ' + \
            append + currentLine[lastIndex:]
        container.append(prepend + ' ' + currentLine)
    openFile.close()

    writeToFile(url+'-after.txt', container)

# create dictionary #


def createDictionaryUnigram():
    d = dict()  # my dictionary

    openFile = open('brown-train-after.txt', 'r')
    openRead = openFile.readlines()

    for currentLine in openRead:
        for oneString in currentLine.split(' '):
            if oneString in d:
                d[oneString] += 1
            else:
                d[oneString] = 1

    writeDictToFile('dictionary-unigram-before-unk-dataset', d)
    return d


def createDictionaryBigram():
    d = dict()  # my dictionary

    openFile = open('brown-train-after.txt', 'r')
    openRead = openFile.readlines()

    for currentLine in openRead:
        split = currentLine.split(' ')

        for index in range(len(split) - 1):
            combinedString = split[index] + ',' + split[index+1]
            if combinedString in d:
                d[combinedString] += 1
            else:
                d[combinedString] = 1

    writeDictToFile('dictionary-bigram-before-unk-dataset', d)
    return d

def writeDictToFile(url, d):
    f = open(url + '.txt', 'w')
    f.write(str(d))
    f.close

# replacing the word with <unk>


def replaceOccuring():
    d = createDictionaryUnigram()  # my dictionary
    print('--Replacing the word occured once in brown-train file with <unk>--')
    replaceOccuringOnce(d, 'brown-train-after')

    print('--Replacing the word not appeared in brown-test file with <unk>--')
    replaceNotOccuring(d, 'brown-test-after')

    print('--Replacing the word not appeared in brown-test file with <unk>--')
    replaceNotOccuring(d, 'learner-test-after')


def replaceOccuringOnce(d, url):
    # REPLACE ALL WORD OCCURING IN TRAINING DATA ONCE WITH THE TOKEN UNK
    # Reading from the file
    openFile = open(url + '.txt', 'r')
    openRead = openFile.readlines()

    container = []

    # REPLACE THE WORD WITH UNKNOWN
    for currentLine in openRead:
        # print(currentLine)
        txt = ''
        for oneString in currentLine.split(' '):
            if oneString == '<s>':
                txt = oneString
            elif d.get(oneString) == 1:
                txt = txt + ' <unk>'
            else:
                txt = txt + ' ' + oneString
        container.append(txt)
    openFile.close()

    writeToFile(url+'-replaced-unk.txt', container)


def replaceNotOccuring(d, url):
    # REPLACE ALL WORD OCCURING IN TRAINING DATA ONCE WITH THE TOKEN UNK
    # Reading from the file
    openFile = open(url + '.txt', 'r')
    openRead = openFile.readlines()

    container = []

    # REPLACE THE WORD WITH UNKNOWN
    for currentLine in openRead:
        # print(currentLine)
        txt = ''
        for key in currentLine.split(' '):
            if key == '<s>':
                txt = key
            elif key not in d.keys():
                txt = txt + ' <unk>'
            else:
                txt = txt + ' ' + key
        container.append(txt)
    openFile.close()

    writeToFile(url + '-replaced-unk.txt', container)


def questionOne():
    mySet = createSet('brown-train-after-replaced-unk')  # my set
    print('Question 1: ', len(mySet))

def questionTwo():
    count = 0
    openFile = open('brown-train-after-replaced-unk.txt', 'r')
    openRead = openFile.readlines()
    for currentLine in openRead:
        count = count + len(currentLine.split(' '))
    print('Question 2: ', count)


def questionThree():
    myDict = createDictionaryUnigram()

    # ** BROWN-TEST ** #
    brownSet = createSet('brown-test-after') 
    countTokenAppearsBrownTest = countTokens(myDict, 'brown-test-after')
    countTypesAppearBrownTest = countTypes(myDict, brownSet)
    sizeBrownTest = countSize('brown-test-after')

    # ** LEARNER-TEST ** #
    learnerSet = createSet('learner-test-after')
    countTypesAppearLearnerTest = countTypes(myDict, learnerSet) 
    countTokenAppearsLearnerTest = countTokens(myDict, 'learner-test-after')
    sizeLearnerTest = countSize('learner-test-after')

    print(countTokenAppearsBrownTest, ' count token appears brown test')
    print(countTypesAppearBrownTest, ' count types appears brown test')
    print(sizeBrownTest, ' size of brown test')

    print(countTypesAppearLearnerTest, ' count type appears learner test')
    print(countTokenAppearsLearnerTest, ' count token appears learner test')
    print(sizeLearnerTest, ' size of learner test')


def createSet(url):
     # CREATING SET FOR TYPES (UNIQUE )
    thisSet = set()  # my set
    openFile = open(url + '.txt', 'r')
    openRead = openFile.readlines()

    for currentLine in openRead:
        for oneString in currentLine.split(' '):
            if oneString not in thisSet:
                thisSet.add(oneString)

    return thisSet

def countTypes(myDict, mySet):
    count = 0
    for item in mySet:
        if item not in myDict:
            count = count + 1
    
    return count

def countTokens(myDict, url):
    count = 0
    openFile = open(url + '.txt', 'r')
    openRead = openFile.readlines()
    # word types (unique)
    for currentLine in openRead:
        for key in currentLine.split(' '):
            if key not in myDict.keys():
                count = count + 1

    openFile.close()
    return count

def countSize(url):
    count = 0
    openFile = open(url + '.txt', 'r')
    openRead = openFile.readlines()
    # word types (unique)
    for currentLine in openRead:
        count = count + len(currentLine.split(' '))

    openFile.close()
    return count