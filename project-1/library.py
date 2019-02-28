def writeToFile(url, container):
    bt = open(url, 'w')
    for string in container:
        bt.write(string)
    bt.close()

# padding sentences


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
            append + ' ' + currentLine[lastIndex:]
        container.append(prepend + ' ' + currentLine)
    openFile.close()

    writeToFile(url+'-after.txt', container)

# create dictionary


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

    f = open('dictionary-unigram-before-unk-dataset.txt', 'w')
    f.write(str(d))
    f.close

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

    f = open('dictionary-bigram-before-unk-dataset.txt', 'w')
    f.write(str(d))
    f.close

    return d

# replacing the word with <unk>


def replaceOccuring():
    d = createDictionaryUnigram()  # my dictionary
    print('--Replacing the word occured once in brown-train file with unk--')
    replaceOccuringOnce(d, 'brown-train-after')

    print('--Replacing the word not appeared in brown-test file with unk--')
    replaceNotOccuring(d, 'brown-test-after')

    print('--Replacing the word not appeared in brown-test file with unk--')
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
        currentLine = currentLine.lower()  # lowecase everything
        for oneString in currentLine.split(' '):
            if d.get(oneString) == 1:
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
        currentLine = currentLine.lower()  # lowecase everything
        for key in currentLine.split(' '):
            if key not in d.keys():
                txt = txt + ' <unk>'
            else:
                txt = txt + ' ' + key
        container.append(txt)
    openFile.close()

    writeToFile(url + '-replaced-unk.txt', container)


def questionOne():
    mySet = set()  # my set
    # print(len(mySet))
    openFile = open('brown-train-after-replaced-unk.txt', 'r')
    openRead = openFile.readlines()

    for currentLine in openRead:
        for oneString in currentLine.split(' '):
            if oneString not in mySet:
                mySet.add(oneString)

    print('Question 1:')
    print(len(mySet))


def questionTwo():
    count1 = 0
    count2 = 0

    openFile = open('brown-train-after-replaced-unk.txt', 'r')
    openRead = openFile.readlines()

    for currentLine in openRead:
        for oneString in currentLine.split(' '):
            # print(oneString)
            count1 = count1 + 1

    d = dict()
    openFile = open('brown-train.txt', 'r')
    openRead = openFile.readlines()

    for currentLine in openRead:
        for oneString in currentLine.split(' '):
            if oneString in d:
                d[oneString] += 1
            else:
                d[oneString] = 1

    for value in d.values():
        count2 = count2 + value

    print('Question 2:')
    print(count1)
    print(count2)


def questionThree():
    d = createDictionaryUnigram()

    # ** BROWN-TEST ** #
    countTokenAppearsBrownTest = 0
    countTypesAppearBrownTest = 0
    sizeBrownTest = 0

    # CREATING SET FOR TYPES (UNIQUE )
    brownSet = set()  # my set
    openFile = open('brown-test-after.txt', 'r')
    openRead = openFile.readlines()

    for currentLine in openRead:
        for oneString in currentLine.split(' '):
            if oneString not in brownSet:
                brownSet.add(oneString)

    openFile = open('brown-test-after' + '.txt', 'r')
    openRead = openFile.readlines()
    # word types (unique)
    for currentLine in openRead:
        sizeBrownTest = sizeBrownTest + \
            len(currentLine.split(' '))
        for key in currentLine.split(' '):
            if key not in d.keys():
                countTokenAppearsBrownTest = countTokenAppearsBrownTest + 1

    for item in brownSet:
        if item not in d:
            countTypesAppearBrownTest = countTypesAppearBrownTest + 1

    openFile.close()

    # ** LEARNER-TEST ** #
    countTypesAppearLearnerTest = 0
    countTokenAppearsLearnerTest = 0
    sizeLearnerTest = 0

    # CREATING SET FOR TYPES (UNIQUE )
    learnerSet = set()  # my set
    openFile = open('learner-test-after.txt', 'r')
    openRead = openFile.readlines()

    for currentLine in openRead:
        for oneString in currentLine.split(' '):
            if oneString not in learnerSet:
                learnerSet.add(oneString)

    openFile = open('learner-test-after' + '.txt', 'r')
    openRead = openFile.readlines()

    # word types (unique)
    for currentLine in openRead:
        sizeLearnerTest = sizeLearnerTest + \
            len(currentLine.split(' '))
        for key in currentLine.split(' '):
            if key not in d.keys():
                countTokenAppearsLearnerTest = countTokenAppearsLearnerTest + 1

    for item in learnerSet:
        if item not in d:
            countTypesAppearLearnerTest = countTypesAppearLearnerTest + 1

    openFile.close()

    print(countTokenAppearsBrownTest, ' count token appears brown test')
    print(countTypesAppearBrownTest, ' count types appears brown test')
    print(sizeBrownTest, ' size of brown test')

    print(countTypesAppearLearnerTest, ' count type appears learner test')
    print(countTokenAppearsLearnerTest, ' count token appears learner test')
    print(sizeLearnerTest, ' size of learner test')


def createSet():
     # CREATING SET FOR TYPES (UNIQUE )
    thisSet = set()  # my set
    openFile = open('brown-test-after.txt', 'r')
    openRead = openFile.readlines()

    for currentLine in openRead:
        for oneString in currentLine.split(' '):
            if oneString not in thisSet:
                thisSet.add(oneString)

    return thisSet
