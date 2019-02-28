#import this so when I divide number it would return float, for python 2.7
from __future__ import division

def writeToFile(url, container):
    bt = open(url, 'w')
    for string in container:
        bt.write(string)
    bt.close()

#-- padding sentences --#
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
        currentLine = currentLine.lower()  # lowercase everything
        lastIndex = len(currentLine) - 1
        currentLine = currentLine[:lastIndex] + ' ' + \
            append + currentLine[lastIndex:]
        container.append(prepend + ' ' + currentLine)
    openFile.close()

    writeToFile(url+'-after.txt', container)

#-- create dictionary --#
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
    # replace all data occurred in the training data once with <unk>
    openFile = open(url + '.txt', 'r')
    openRead = openFile.readlines()

    container = []

    for currentLine in openRead:
        txt = ''
        for oneString in currentLine.split(' '):
            if oneString == '<s>':
                txt = oneString
            elif d.get(oneString) == 1: # replace the word that appear only once with the word <unk>
                txt = txt + ' <unk>'
            else:
                txt = txt + ' ' + oneString
        container.append(txt)
    openFile.close()

    writeToFile(url+'-replaced-unk.txt', container)

def replaceNotOccuring(d, url):
    # replace all data not occurred in the training data with <unk>
    openFile = open(url + '.txt', 'r')
    openRead = openFile.readlines()

    container = []

    for currentLine in openRead:
        txt = ''
        for key in currentLine.split(' '):
            if key == '<s>':
                txt = key
            elif key not in d.keys(): # replace the word that not appear in the training with <unk>
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
    sizeTraining = countSize('brown-train-after')
    print('Size of training set ', sizeTraining)

    # ** BROWN-TEST ** #
    brownSet = createSet('brown-test-after') 
    countTokenBrownNotAppearsTrainning = countTokens(myDict, 'brown-test-after')
    countTypesBrownNotAppearTraining = countTypes(myDict, brownSet)
    sizeBrownTest = countSize('brown-test-after')

    print(countTokenBrownNotAppearsTrainning, 'token')
    print(countTypesBrownNotAppearTraining, 'type')
    print(sizeBrownTest, 'size')


    # COUNT OF HOW MANY WORD NOT APPEAR / COUNT OF HOW MANY WORD IN TRAINING
    # COUNT OF HOW MANY THOSE ^ / SIZE OF THE TEST
    percentageTokenBrown = countTokenBrownNotAppearsTrainning/sizeTraining

    print(percentageTokenBrown, 'percentage token brown')
    percentageTokenBrown =  (percentageTokenBrown / sizeBrownTest) * 100

    percentageTypesBrown =  (countTypesBrownNotAppearTraining/sizeTraining)
    percentageTypesBrown =  (percentageTypesBrown / sizeBrownTest) * 100

    # ** LEARNER-TEST ** #
    learnerSet = createSet('learner-test-after')
    countTokenLearnerNotAppearsTraining = countTokens(myDict, 'learner-test-after')
    countTypesLearnerNotAppearTraining = countTypes(myDict, learnerSet) 
    sizeLearnerTest = countSize('learner-test-after')

    percentageTokenLearner =  (countTokenLearnerNotAppearsTraining/sizeTraining)
    percentageTokenLearner =  (percentageTokenLearner / sizeLearnerTest) * 100

    percentageTypesLearner =  (countTypesLearnerNotAppearTraining/sizeTraining)
    percentageTypesLearner =  (percentageTypesLearner / sizeLearnerTest) * 100

    #PRINTING OUT

    print(countTokenBrownNotAppearsTrainning, ' count token appears brown test')
    print(countTypesBrownNotAppearTraining, ' count types appears brown test')
    print(sizeBrownTest, ' size of brown test')

    print('Percentage of tokens in Brown not appear in training ', percentageTokenBrown)
    print('Percentage of types in Brown not appear in training ', percentageTypesBrown)

    print(countTypesLearnerNotAppearTraining, ' count type appears learner test')
    print(countTokenLearnerNotAppearsTraining, ' count token appears learner test')
    print(sizeLearnerTest, ' size of learner test')


    print('Percentage of tokens in Learner not appear in training ', percentageTokenLearner)
    print('Percentage of types in Learner not appear in training ', percentageTypesLearner)

# helper function for question 3 #
def createSet(url):
    thisSet = set() 

    openFile = open(url + '.txt', 'r')
    openRead = openFile.readlines()

    for currentLine in openRead:
        for oneString in currentLine.split(' '):
            if oneString not in thisSet:
                thisSet.add(oneString)

    return thisSet

def countTypes(myDict, mySet): #return how many unique value in set, not appear in the map/dictionary
    count = 0
    for item in mySet:
        if item not in myDict:
            count = count + 1
    
    return count

def countTokens(myDict, url): #return how many tokens (all words) in the file not appear in the dict
    count = 0
    openFile = open(url + '.txt', 'r')
    openRead = openFile.readlines()
    for currentLine in openRead:
        for key in currentLine.split(' '):
            if key not in myDict.keys():
                count = count + 1

    openFile.close()
    return count

def countSize(url): #return how many words in a text file
    count = 0
    openFile = open(url + '.txt', 'r')
    openRead = openFile.readlines()
    for currentLine in openRead:
        count = count + len(currentLine.split(' '))

    openFile.close()
    return count
# end of helper function for question 3 #

def questionFour():
    myDict = createDictionaryBigram()
    countTraining = countSizeBigram('brown-train-after-replaced-unk')

    brownUrl = 'brown-test-after-replaced-unk'
    brownSet = createSetBigram(brownUrl)
    countTypesBrownNotInTraining = countTypesBigram(myDict, brownSet)
    countTokenBrownNotInTrainning = countTokensBigram(myDict, brownUrl)
    countBigramInBrown = countSizeBigram(brownUrl)

    learnerUrl = 'learner-test-after-replaced-unk'
    learnerSet = createSetBigram(learnerUrl)
    countTypesLearnerNotInTraining = countTypesBigram(myDict, learnerSet)
    countTokenLearnerNotInTraining = countTokensBigram(myDict, learnerUrl)
    countBigramInLearner = countSizeBigram(learnerUrl)

# helper function for question 4 #
def createSetBigram(url):
    thisSet = set()
    openFile = open(url + '.txt', 'r')
    openRead = openFile.readlines()

    for currentLine in openRead:
        split = currentLine.split(' ')
        for index in range(len(split) - 1):
            combinedString = split[index] + ',' + split[index+1]
            if combinedString not in thisSet:
                thisSet.add(combinedString)
    
    return thisSet

def countTypesBigram(myDict, mySet):

    count = 0
    for item in mySet:
        if item not in myDict:
            count = count + 1

    return count

def countTokensBigram(myDict, url):
    count = 0
    openFile = open(url + '.txt', 'r')
    openRead = openFile.readlines()
    
    for currentLine in openRead:
        split = currentLine.split(' ')
        for index in range(len(split) - 1):
            combinedString = split[index] + ',' + split[index+1]
            # countBigramInBrown = countBigramInBrown + 1
            if combinedString not in myDict:
                count = count + 1
    return count

def countSizeBigram(url):
    count = 0

    openFile = open(url + '.txt', 'r')
    openRead = openFile.readlines()
    for currentLine in openRead:
        split = currentLine.split(' ')
        for index in range(len(split) - 1):
            count = count + 1

    return count
# end of helper function for question 4 # 

