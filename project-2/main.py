from __future__ import division
import library

# ----- --------- -------
# start of total document
trainingTotal = ['Chinese Beijing Chinese', 'Chinese Chinese Shanghai',
                 'Chinese Macao', 'Tokyo Japan Chinese']

trainingTotalBigDocument = library.createBigDocument(trainingTotal)
splittedTrainingTotal = library.createSplitDocument(trainingTotalBigDocument)

dictionaryTotal = library.createDictionary(splittedTrainingTotal)
library.printDictionaryKeyValue(dictionaryTotal)

totalWordInVocabulary = len(dictionaryTotal)
print(totalWordInVocabulary)

# ----- --------- ---------
# start of c class training
trainingClassC = ['Chinese Beijing Chinese',
                  'Chinese Chinese Shanghai', 'Chinese Macao']
trainingClassCBigDocument = library.createBigDocument(trainingClassC)

splittedTrainingClassC = library.createSplitDocument(trainingClassCBigDocument)
totalWordInVocabularyClassC = library.getSizeOfDocument(
    trainingClassCBigDocument)
print(totalWordInVocabularyClassC)

dictionaryClassC = library.createDictionary(splittedTrainingClassC)
library.printDictionaryKeyValue(dictionaryClassC)


# ----- --------- ---------
# start of j class training
trainingClassJ = ['Tokyo Japan Chinese']
trainingClassJBigDocument = library.createBigDocument(trainingClassJ)
splittedTrainingClassJ = library.createSplitDocument(trainingClassJBigDocument)

dictionaryClassJ = library.createDictionary(splittedTrainingClassJ)
library.printDictionaryKeyValue(dictionaryClassJ)

totalWordInVocabularyClassJ = library.getSizeOfDocument(
    trainingClassJBigDocument)
print(totalWordInVocabularyClassJ)

# -------
# example

prob = library.getProbability(
    dictionaryClassC, 'Chinese', totalWordInVocabularyClassC, totalWordInVocabulary)
print('P(Chinese|c) = ' + `prob`)

prob = library.getProbability(
    dictionaryClassC, 'Tokyo', totalWordInVocabularyClassC, totalWordInVocabulary)
print('P(Tokyo|c) = ' + `prob`)


prob = library.getProbability(
    dictionaryClassC, 'Japan', totalWordInVocabularyClassC, totalWordInVocabulary)
print('P(Japan|c) = ' + `prob`)

prob = library.getProbability(
    dictionaryClassJ, 'Chinese', totalWordInVocabularyClassJ, totalWordInVocabulary)

print('P(Chinese|j) = ' + `prob`)

prob = library.getProbability(
    dictionaryClassJ, 'Tokyo', totalWordInVocabularyClassJ, totalWordInVocabulary)
print('P(Tokyo|j) = ' + `prob`)

prob = library.getProbability(
    dictionaryClassJ, 'Japan', totalWordInVocabularyClassJ, totalWordInVocabulary)
print('P(Japan|j) = ' + `prob`)

test = 'Chinese Chinese Chinese Tokyo Japan'
