# take training file, test file, file where the parameters of the resulting model will be saved, and the result itself in own file.
# last line in output file should list the overall accuracy of the classifier on test data
# training and test should've this format: one ex per line, each line corresponds to one example
# first column is the label, other column are feature value

f = open('movie-review-small.NB', 'r+')

place = []
with open('movie-review-small.NB', 'r') as filehandle:
    for line in filehandle:
        currentPlace = line[:-1]
        place.append(currentPlace)

fAction = open('movie-review-small-action.txt', 'w+')
fComedy = open('movie-review-small-comedy.txt', 'w+')

for string in place:
    stringSplitted = string.split(',')
    index = 0
    if stringSplitted[0] == 'comedy':
        for each in stringSplitted:
            if index == 0:
                index = index + 1
                continue
            fComedy.write(each)
        fComedy.write(' ')
    else:
        for each in stringSplitted:
            if index == 0:
                index = index + 1
                continue
            fAction.write(each)
        fAction.write(' ')


f.close()
fAction.close()
fComedy.close()

fAction = open('movie-review-small-action.txt', 'r+')
dictAction = {}
for item in fAction:
    itemSplitted = item.split(" ")
    for eachItem in itemSplitted:
        if eachItem == '':
            continue
        if eachItem in dictAction.keys():
            dictAction[eachItem] = dictAction[eachItem] + 1
        else:
            dictAction[eachItem] = 1

fComedy = open('movie-review-small-comedy.txt', 'r+')
dictComedy = {}
for item in fComedy:
    itemSplitted = item.split(" ")
    for eachItem in itemSplitted:
        if eachItem == '':
            continue
        if eachItem in dictAction.keys():
            dictComedy[eachItem] = dictAction[eachItem] + 1
        else:
            dictComedy[eachItem] = 1

print('Dictionary in action')
print(dictAction)
print('Dictionary in comedy')
print(dictComedy)


def NB(trainingFile, testFile, fileParameter, outputFile):
    print('Naive Bayes Algorithm')
