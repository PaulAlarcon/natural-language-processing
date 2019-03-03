# import this so when I divide number it would return float, for python 2.7
from __future__ import division
from math import log


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
    container = []

    # reading from the file
    openFile = open(url + '.txt', 'r')
    openRead = openFile.readlines()

    for currentLine in openRead:
        currentLine = currentLine.lower()  # lowercase everything
        lastIndex = len(currentLine) - 1
        currentLine = currentLine[:lastIndex] + ' ' + \
            '</s>' + ' ' + currentLine[lastIndex:]
        container.append('<s>' + ' ' + currentLine)
    openFile.close()

    writeToFile(url+'-after.txt', container)

#-- create dictionary --#


def createDictionaryUnigram(url):
    d = dict()  # my dictionary

    openFile = open(url + '.txt', 'r')
    openRead = openFile.readlines()

    for currentLine in openRead:
        for oneString in currentLine.split(' '):
            if oneString in d:
                d[oneString] += 1
            else:
                d[oneString] = 1

    writeDictToFile('dictionary-unigram-' + url, d)
    return d


def createDictionaryBigram(url):
    d = dict()  # my dictionary

    openFile = open(url + '.txt', 'r')
    openRead = openFile.readlines()

    for currentLine in openRead:
        split = currentLine.split(' ')

        for index in range(len(split) - 1):
            combinedString = split[index] + ',' + split[index+1]
            if combinedString in d:
                d[combinedString] += 1
            else:
                d[combinedString] = 1

    writeDictToFile('dictionary-bigram-' + url, d)
    return d


def createDictionaryBigramSmoothing():
    d = createDictionaryBigram('brown-train-after-replaced-unk')

    for key in d:
        d[key] = d[key] + 1

    writeDictToFile('dictionary-bigram-smoothing-before-unk-dataset', d)
    return d


def writeDictToFile(url, d):
    f = open(url + '.txt', 'w')
    f.write(str(d))
    f.close

# replacing the word with <unk>


def replaceOccuring():
    d = createDictionaryUnigram('brown-train-after')  # my dictionary
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
            elif d.get(oneString) == 1:  # replace the word that appear only once with the word <unk>
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
            elif key not in d.keys():  # replace the word that not appear in the training with <unk>
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
    count = countSize('brown-train-after-replaced-unk')
    print('Question 2: ', count)


def questionThree():
    print('Question 3:')
    myDict = createDictionaryUnigram('brown-train-after')
    percentageQ3(myDict, 'brown-test-after')
    percentageQ3(myDict, 'learner-test-after')

# helper function for question 3 #


def percentageQ3(myDict, url):
    mySet = createSet(url)
    sizeTypes = len(mySet)  # size of set (unique types)
    countTokenNotAppearsTrainning = countTokens(myDict, url)
    countTypesNotAppearsTraining = countTypes(myDict, mySet)
    sizeTokens = countSize(url)  # size of token
    printPercentage(url, sizeTypes, sizeTokens, countTokenNotAppearsTrainning, countTypesNotAppearsTraining)

def createSet(url):
    thisSet = set()

    openFile = open(url + '.txt', 'r')
    openRead = openFile.readlines()

    for currentLine in openRead:
        for oneString in currentLine.split(' '):
            if oneString not in thisSet:
                thisSet.add(oneString)

    return thisSet


# return how many unique value in set, not appear in the map/dictionary
def countTypes(myDict, mySet):
    count = 0
    for item in mySet:
        if item not in myDict:
            count = count + 1

    return count


# return how many tokens (all words) in the file not appear in the dict
def countTokens(myDict, url):
    count = 0
    openFile = open(url + '.txt', 'r')
    openRead = openFile.readlines()
    for currentLine in openRead:
        for key in currentLine.split(' '):
            if key not in myDict.keys():
                count = count + 1

    openFile.close()
    return count


def countSize(url):  # return how many words in a text file
    count = 0
    openFile = open(url + '.txt', 'r')
    openRead = openFile.readlines()
    for currentLine in openRead:
        splittedSentence = currentLine.split(' ')
        for word in splittedSentence:
            if word != '\n':
                count = count + 1

    openFile.close()
    return count
# end of helper function for question 3 #


def questionFour():
    print('Question 4:')
    myDict = createDictionaryBigram('brown-train-after-replaced-unk')

    percentageQ4(myDict, 'brown-test-after-replaced-unk')
    percentageQ4(myDict, 'learner-test-after-replaced-unk')

# helper function for question 4 #


def percentageQ4(myDict, url):
    mySet = createSetBigram(url)
    sizeTypes = len(mySet)
    countTypesNotInTraining = countTypesBigram(myDict, mySet)
    countTokenNotInTraining = countTokensBigram(myDict, url)
    sizeTokens = countSizeBigram(url)
    printPercentage(url, sizeTypes, sizeTokens, countTokenNotInTraining, countTypesNotInTraining)

def printPercentage(url, sizeTypes, sizeTokens, countTokenNotInTraining, countTypesNotInTraining):
    print('Size of types in ' + url + '=', sizeTypes)
    print('Size of tokens in ' + url + '=', sizeTokens)

    print('How many tokens in ' + url + ' not appear in training = ',
          countTokenNotInTraining)
    print('How many types in ' + url + ' not appear in training = ',
          countTypesNotInTraining)

    percentageToken = countTokenNotInTraining/sizeTokens
    print('How many percentage token in ' + url + ' = ', percentageToken)

    percentageTypes = (countTypesNotInTraining/sizeTypes)
    print('How many percentage types in ' + url + ' = ', percentageTypes)
    
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

    unigramDict = createDictionaryUnigram('brown-train-after')

    for currentLine in openRead:
        split = currentLine.split(' ')
        for index in range(len(split) - 1):
            if split[index] == '<unk>':
                if split[index+1] not in unigramDict:
                    count = count + 1
            elif split[index+1] == '<unk>':
                if split[index] not in unigramDict:
                    count = count + 1
            else:
                combinedString = split[index] + ',' + split[index+1]
                if combinedString not in myDict:
                    count = count + 1
    return count


def countSizeBigram(url):
    count = 0

    openFile = open(url + '.txt', 'r')
    openRead = openFile.readlines()
    for currentLine in openRead:
        split = currentLine.split(' ')
        # count = count + len(split)
        for index in range(len(split)):
            if split[index] == '\n' or split[index + 1] == '\n':
                continue
            count = count + 1

    return count
# end of helper function for question 4 #


def questionFive():
    dictUnigram = createDictionaryUnigram('brown-train-after')
    sizeOfToken = countSize('brown-train-after')

    fSentence = 'He was laughed off the screen .'
    sSentence = 'There was no compulsion behind them .'
    tSentence = 'I look forward to hearing your reply .'

    probabilitySentenceUnigram(fSentence, dictUnigram, sizeOfToken)
    probabilitySentenceUnigram(sSentence, dictUnigram, sizeOfToken)
    probabilitySentenceUnigram(tSentence, dictUnigram, sizeOfToken)

    dictBigram = createDictionaryBigram('brown-train-after-replaced-unk')

    probabilitySentenceBigram(fSentence, dictBigram, sizeOfToken)
    probabilitySentenceBigram(sSentence, dictBigram, sizeOfToken)
    probabilitySentenceBigram(tSentence, dictBigram, sizeOfToken)

    dictBigramSmoothing = createDictionaryBigramSmoothing()

    probabilitySentenceBigramSmoothing(
        fSentence, dictBigramSmoothing, sizeOfToken)
    probabilitySentenceBigramSmoothing(
        sSentence, dictBigramSmoothing, sizeOfToken)
    probabilitySentenceBigramSmoothing(
        tSentence, dictBigramSmoothing, sizeOfToken)


def modifiedSentence(string, myDict):
    str = '<s> ' + string.lower() + ' </s>'
    returnedStr = ''
    for item in str.split(' '):
        if item not in myDict:
            returnedStr = returnedStr + ' <unk> '
        else:
            returnedStr = returnedStr + item
    return str


def probabilitySentenceUnigram(string, myDict, size):
    sentence = modifiedSentence(string, myDict)
    sentenceSplitted = sentence.split(' ')
    # print(sentenceSplitted)
    sum = 0

    for string in sentenceSplitted:
        if string == '<s>':
            continue
        # print(string)
        if string in myDict:
            # print(string, myDict[string])
            sum += log(myDict[string]/size, 2)
    sum = sum / len(sentenceSplitted)
    print('Probability unigram for ' + sentence, sum)


def probabilitySentenceBigram(string, myDict, size):
    sentence = modifiedSentence(string, myDict)
    sentenceSplitted = sentence.split(' ')

    sum = 0
    for index in range(len(sentenceSplitted) - 1):
        combinedString = sentenceSplitted[index] + \
            ',' + sentenceSplitted[index+1]
        # print(combinedString)
        if combinedString in myDict:
            # print(combinedString, myDict[combinedString])
            sum += log(myDict[combinedString]/size, 2)

    sum = sum / len(sentenceSplitted)
    print('Probability bigram for ' + sentence, sum)
    return sum


def probabilitySentenceBigramSmoothing(string, myDict, size):
    sentence = modifiedSentence(string, myDict)
    sentenceSplitted = sentence.split(' ')

    sum = 0
    for index in range(len(sentenceSplitted) - 1):
        combinedString = sentenceSplitted[index] + \
            ',' + sentenceSplitted[index+1]
        # print(combinedString)
        if combinedString in myDict:
            # print(combinedString, myDict[combinedString])
            sum += log(myDict[combinedString]/size, 2)

    sum = sum / len(sentenceSplitted)
    print('Probability bigram smoothing for ' + sentence, sum)
    return sum


def questionSix():
    print('Question 6:')
    myDict = createDictionaryBigram('brown-train-after-replaced-unk')
    fSentence = 'He was laughed off the screen'
    sSentence = 'There was no compulsion behind them'
    tSentence = 'I look forward to hearing your reply'

    print(modifiedSentence(fSentence, myDict))
    print(modifiedSentence(sSentence, myDict))
    print(modifiedSentence(tSentence, myDict))


def perplexity(string):
    print(string)
