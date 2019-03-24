from __future__ import division
import exampleLibrary

# ----- --------- -------
# start of total document
trainingTotal = ['Chinese Beijing Chinese', 'Chinese Chinese Shanghai',
                 'Chinese Macao', 'Tokyo Japan Chinese']

trainingTotalBigDocument = exampleLibrary.createBigDocument(trainingTotal)
splittedTrainingTotal = exampleLibrary.createSplitDocument(
    trainingTotalBigDocument)

dictionaryTotal = exampleLibrary.createDictionary(splittedTrainingTotal)
exampleLibrary.printDictionaryKeyValue(dictionaryTotal)

totalWordInVocabulary = len(dictionaryTotal)
print(totalWordInVocabulary)

# ----- --------- ---------
# start of c class training
trainingClassC = ['Chinese Beijing Chinese',
                  'Chinese Chinese Shanghai', 'Chinese Macao']
trainingClassCBigDocument = exampleLibrary.createBigDocument(trainingClassC)

splittedTrainingClassC = exampleLibrary.createSplitDocument(
    trainingClassCBigDocument)
totalWordInVocabularyClassC = exampleLibrary.getSizeOfDocument(
    trainingClassCBigDocument)
print(totalWordInVocabularyClassC)

dictionaryClassC = exampleLibrary.createDictionary(splittedTrainingClassC)
exampleLibrary.printDictionaryKeyValue(dictionaryClassC)


# ----- --------- ---------
# start of j class training
trainingClassJ = ['Tokyo Japan Chinese']
trainingClassJBigDocument = exampleLibrary.createBigDocument(trainingClassJ)
splittedTrainingClassJ = exampleLibrary.createSplitDocument(
    trainingClassJBigDocument)

dictionaryClassJ = exampleLibrary.createDictionary(splittedTrainingClassJ)
exampleLibrary.printDictionaryKeyValue(dictionaryClassJ)

totalWordInVocabularyClassJ = exampleLibrary.getSizeOfDocument(
    trainingClassJBigDocument)
print(totalWordInVocabularyClassJ)

# -------
# example

prob = exampleLibrary.getProbability(
    dictionaryClassC, 'Chinese', totalWordInVocabularyClassC, totalWordInVocabulary)
print('P(Chinese|c) = ' + `prob`)

prob = exampleLibrary.getProbability(
    dictionaryClassC, 'Tokyo', totalWordInVocabularyClassC, totalWordInVocabulary)
print('P(Tokyo|c) = ' + `prob`)


prob = exampleLibrary.getProbability(
    dictionaryClassC, 'Japan', totalWordInVocabularyClassC, totalWordInVocabulary)
print('P(Japan|c) = ' + `prob`)

prob = exampleLibrary.getProbability(
    dictionaryClassJ, 'Chinese', totalWordInVocabularyClassJ, totalWordInVocabulary)

print('P(Chinese|j) = ' + `prob`)

prob = exampleLibrary.getProbability(
    dictionaryClassJ, 'Tokyo', totalWordInVocabularyClassJ, totalWordInVocabulary)
print('P(Tokyo|j) = ' + `prob`)

prob = exampleLibrary.getProbability(
    dictionaryClassJ, 'Japan', totalWordInVocabularyClassJ, totalWordInVocabulary)
print('P(Japan|j) = ' + `prob`)

test = 'Chinese Chinese Chinese Tokyo Japan'
