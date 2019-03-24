from __future__ import division


def createBigDocument(sentenceArray):
    trainingOneDoc = ''
    # combining into one big document
    for str in sentenceArray:
        trainingOneDoc = trainingOneDoc + str + ' '
    print('The training now is: ' + trainingOneDoc)
    return trainingOneDoc


def createSplitDocument(trainingOneDoc):
    splitted = trainingOneDoc.split(' ')
    print('The training one log document is splitted into')
    print(splitted)
    return splitted


def createDictionary(data):
    dictionary = {}
    for str in data:
        if str == "":
            continue
        if str in dictionary:
            dictionary[str] = dictionary[str] + 1
        else:
            dictionary[str] = 1

    return dictionary


def printDictionaryKeyValue(data):
    print('Start the dictionary iteration')
    for key in data:
        result = `data[key]` + ' ' + key
        print(result)


def getSizeOfDocument(data):
    return len(data.split(" "))


def getProbability(dict, str, totalWordInClass, totalWordInVocabulary):
    result = 0
    if str not in dict:
        result = 1 / (totalWordInClass + totalWordInVocabulary)
    else:
        result = (dict[str] + 1) / \
            (totalWordInClass + totalWordInVocabulary)

    return result
