# import this so when I divide number it would return float, for python 2.7
from __future__ import division
import math


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

    writeDictToFile('dictionary-bigram-smoothing', d)
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
    print('Question 1:')
    print('Unique words in training corpus: ', len(mySet))
    print('\n')


def questionTwo():
    count = countSize('brown-train-after-replaced-unk')
    print('Question 2:')
    print('Token words in training corpus: ', count)
    print('\n')


def questionThree():
    print('Question 3:')
    myDict = createDictionaryUnigram('brown-train-after')
    percentageQ3(myDict, 'brown-test-after')
    percentageQ3(myDict, 'learner-test-after')
    print('\n')

# helper function for question 3 #


def percentageQ3(myDict, url):
    mySet = createSet(url)
    sizeTypes = len(mySet)  # size of set (unique types)
    countTokenNotAppearsTrainning = countTokens(myDict, url)
    countTypesNotAppearsTraining = countTypes(myDict, mySet)
    sizeTokens = countSize(url)  # size of token
    printPercentage(url, sizeTypes, sizeTokens,
                    countTokenNotAppearsTrainning, countTypesNotAppearsTraining)


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
    print('\n')

# helper function for question 4 #


def percentageQ4(myDict, url):
    mySet = createSetBigram(url)
    sizeTypes = len(mySet)
    countTypesNotInTraining = countTypesBigram(myDict, mySet)
    countTokenNotInTraining = countTokensBigram(myDict, url)
    sizeTokens = countSizeBigram(url)
    printPercentage(url, sizeTypes, sizeTokens,
                    countTokenNotInTraining, countTypesNotInTraining)


def printPercentage(url, sizeTypes, sizeTokens, countTokenNotInTraining, countTypesNotInTraining):
    print('Size of types in ' + url + '=', sizeTypes)
    print('Size of tokens in ' + url + '=', sizeTokens)
    print('\n')

    print('How many tokens in ' + url + ' not appear in training = ',
          countTokenNotInTraining)
    print('How many types in ' + url + ' not appear in training = ',
          countTypesNotInTraining)
    print('\n')

    percentageToken = countTokenNotInTraining/sizeTokens
    print('How many percentage token in ' + url + ' = ', percentageToken)
    percentageTypes = (countTypesNotInTraining/sizeTypes)
    print('How many percentage types in ' + url + ' = ', percentageTypes)
    print('\n')


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
    print('Question 5: ')
    dictUnigram = createDictionaryUnigram('brown-train-after-replaced-unk')
    sizeOfToken = countSize('brown-train-after-replaced-unk')

    fSentence = 'He was laughed off the screen .'
    sSentence = 'There was no compulsion behind them .'
    tSentence = 'I look forward to hearing your reply .'

    fSentence = modifiedSentence(fSentence, dictUnigram)
    sSentence = modifiedSentence(sSentence, dictUnigram)
    tSentence = modifiedSentence(tSentence, dictUnigram)

    probabilitySentenceUnigram(fSentence, dictUnigram, sizeOfToken)
    probabilitySentenceUnigram(sSentence, dictUnigram, sizeOfToken)
    probabilitySentenceUnigram(tSentence, dictUnigram, sizeOfToken)
    print('\n')
    dictBigram = createDictionaryBigram('brown-train-after-replaced-unk')

    probabilitySentenceBigram(fSentence, dictBigram, sizeOfToken)
    probabilitySentenceBigram(sSentence, dictBigram, sizeOfToken)
    probabilitySentenceBigram(tSentence, dictBigram, sizeOfToken)
    print('\n')

    probabilitySentenceBigramSmoothing(
        fSentence, dictBigram, sizeOfToken)
    probabilitySentenceBigramSmoothing(
        sSentence, dictBigram, sizeOfToken)
    probabilitySentenceBigramSmoothing(
        tSentence, dictBigram, sizeOfToken)
    print('\n')


def modifiedSentence(string, myDict):
    str = '<s> ' + string.lower() + ' </s>'
    returnedStr = ''
    for item in str.split(' '):
        if item not in myDict:
            returnedStr = returnedStr + ' <unk>'
        else:
            returnedStr = returnedStr + ' ' + item
    return returnedStr


def probabilitySentenceUnigram(sentence, myDict, size):
    sentenceSplitted = sentence.split(' ')
    # print(sentenceSplitted)
    sum = 0

    for string in sentenceSplitted:
        if string == '<s>':
            continue
        # print(string)
        if string in myDict:
            # print(string, myDict[string])
            sum += math.log(myDict[string]/size, 2)

    sum = sum / len(sentenceSplitted)
    print('Probability unigram for ' + sentence, sum)


def probabilitySentenceBigram(sentence, myDict, size):
    sentenceSplitted = sentence.split(' ')

    sum = 0
    for index in range(len(sentenceSplitted) - 1):
        combinedString = sentenceSplitted[index] + \
            ',' + sentenceSplitted[index+1]
        # print(combinedString)
        if combinedString in myDict:
            # print(combinedString, myDict[combinedString])
            # print(log(myDict[combinedString]/size, 2))
            sum += math.log(myDict[combinedString]/size, 2)
            # print('sum ', sum)

    # print('done')
    sum = sum / len(sentenceSplitted)
    print('Probability bigram for ' + sentence, sum)
    return sum


def probabilitySentenceBigramSmoothing(sentence, myDict, size):
    sentenceSplitted = sentence.split(' ')

    sum = 0
    for index in range(len(sentenceSplitted) - 1):
        combinedString = sentenceSplitted[index] + \
            ',' + sentenceSplitted[index+1]
        # print(combinedString)
        if combinedString in myDict:
            # print(combinedString, myDict[combinedString])
            sum += math.log((myDict[combinedString] +
                             1)/(size + len(myDict)), 2)

    sum = sum / len(sentenceSplitted)
    print('Probability bigram smoothing for ' + sentence, sum)
    return sum


def questionSix():
    print('Question 6:')
    dictUnigram = createDictionaryUnigram('brown-train-after-replaced-unk')
    dictBigram = createDictionaryBigram('brown-train-after-replaced-unk')
    sizeOfToken = countSize('brown-train-after-replaced-unk')

    fSentence = 'He was laughed off the screen'
    sSentence = 'There was no compulsion behind them'
    tSentence = 'I look forward to hearing your reply'

    fSentence = modifiedSentence(fSentence, dictUnigram)
    sSentence = modifiedSentence(sSentence, dictUnigram)
    tSentence = modifiedSentence(tSentence, dictUnigram)

    perplexityUnigram(fSentence, dictUnigram, sizeOfToken)
    perplexityUnigram(sSentence, dictUnigram, sizeOfToken)
    perplexityUnigram(tSentence, dictUnigram, sizeOfToken)

    print('\n')
    sizeOfBigram = countSizeBigram('brown-train-after-replaced-unk')
    perplexityBigram(fSentence, dictBigram, sizeOfBigram)
    perplexityBigram(sSentence, dictBigram, sizeOfBigram)
    perplexityBigram(tSentence, dictBigram, sizeOfBigram)

    print('\n')

    perplexityBigramSmoothing(fSentence, dictBigram, sizeOfBigram)
    perplexityBigramSmoothing(sSentence, dictBigram, sizeOfBigram)
    perplexityBigramSmoothing(tSentence, dictBigram, sizeOfBigram)


def perplexityUnigram(sentence, myDict, size):
    sentenceSplitted = sentence.split(' ')
    sum = 0

    for string in sentenceSplitted:
        if string == '<s>':
            continue
        if string in myDict:
            sum += math.log(myDict[string]/size, 2)
    sum = sum / len(sentenceSplitted)

    sum = math.log(sum * -1, 2)
    print('Unigram perplexity for ' + sentence + ' = ', sum)


def perplexityBigram(sentence, myDict, size):
    sentenceSplitted = sentence.split(' ')
    sum = 0
    for index in range(len(sentenceSplitted) - 1):
        combinedString = sentenceSplitted[index] + \
            ',' + sentenceSplitted[index+1]
        # print(combinedString)
        if combinedString in myDict:
            # print(combinedString, myDict[combinedString])
            sum += math.log(myDict[combinedString]/size, 2)

    sum = sum / len(sentenceSplitted)
    sum = math.log(sum * -1, 2)
    print('Bigram perplexity for ' + sentence + ' = ', sum)
    return sum


def perplexityBigramSmoothing(sentence, myDict, size):
    sentenceSplitted = sentence.split(' ')

    sum = 0
    for index in range(len(sentenceSplitted) - 1):
        combinedString = sentenceSplitted[index] + \
            ',' + sentenceSplitted[index+1]
        # print(combinedString)
        if combinedString in myDict:
            # print(combinedString, myDict[combinedString])
            sum += math.log((myDict[combinedString] +
                             1)/(size + len(myDict)), 2)

    sum = sum / len(sentenceSplitted)
    sum = math.log(sum * -1, 2)
    print('Bigram smoothing perplexity for ' + sentence + ' = ', sum)
    return sum


def questionSeven():
    print('Question 7:')
    perplexityQ7('brown-test-after-replaced-unk')
    print('\n')
    perplexityQ7('learner-test-after-replaced-unk')


def perplexityQ7(url):
    perplexityQ7Unigram(url)
    perplexityQ7Bigram(url)
    perplexityQ7BigramSmoothing(url)


def perplexityQ7Unigram(url):
    dictUnigram = createDictionaryUnigram('brown-train-after-replaced-unk')
    size = countSize('brown-train-after-replaced-unk')
    sum = 0

    openFile = open(url + '.txt', 'r')
    openRead = openFile.readlines()

    for currentLine in openRead:
        sentenceSplitted = currentLine.split(' ')

        for string in sentenceSplitted:
            if string == '<s>':
                continue
            if string in dictUnigram:
                sum += math.log(dictUnigram[string]/size, 2)
        # sum = sum / len(sentenceSplitted)
    print(len(openRead))
    sum = sum / len(openRead)
    sum = math.log(sum * -1, 2)
    print('Unigram perplexity for ' + url + ' = ', sum)


def perplexityQ7Bigram(url):
    dictBigram = createDictionaryBigram('brown-train-after-replaced-unk')
    size = countSize('brown-train-after-replaced-unk')

    openFile = open(url + '.txt', 'r')
    openRead = openFile.readlines()

    for currentLine in openRead:
        sentenceSplitted = currentLine.split(' ')
        sum = 0
        for index in range(len(sentenceSplitted) - 1):
            combinedString = sentenceSplitted[index] + \
                ',' + sentenceSplitted[index+1]
            # print(combinedString)
            if combinedString in dictBigram:
                # print(combinedString, myDict[combinedString])
                sum += math.log(dictBigram[combinedString]/size, 2)

    sum = sum / len(openRead)
    sum = math.log(sum * -1, 2)
    print('Bigram perplexity for ' + url + ' = ', sum)


def perplexityQ7BigramSmoothing(url):
    dictBigram = createDictionaryBigram('brown-train-after-replaced-unk')
    size = countSize('brown-train-after-replaced-unk')

    openFile = open(url + '.txt', 'r')
    openRead = openFile.readlines()

    for currentLine in openRead:
        sentenceSplitted = currentLine.split(' ')
        sum = 0
        for index in range(len(sentenceSplitted) - 1):
            combinedString = sentenceSplitted[index] + \
                ',' + sentenceSplitted[index+1]
            # print(combinedString)
            if combinedString in dictBigram:
                # print(combinedString, myDict[combinedString])
                sum += math.log((dictBigram[combinedString] +
                                 1)/(size + len(dictBigram)), 2)

    sum = sum / len(openRead)
    sum = math.log(sum * -1, 2)
    print('Bigram smoothing perplexity for ' + url + ' = ', sum)
