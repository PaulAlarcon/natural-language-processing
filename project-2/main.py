training = ['Chinese Beijing Chinese', 'Chinese Chinese Shanghai',
            'Chinese Macao', 'Tokyo Japan Chinese']

trainingOneDoc = ''
# combining into one big document
for str in training:
    trainingOneDoc = trainingOneDoc + str + ' '
print('The training now is: ')
print(trainingOneDoc)

splittedTraining = trainingOneDoc.split(' ')
print('The training one log document is splitted into')
print(splittedTraining)

dictionary = {}
for str in splittedTraining:
    if str == "":
        continue
    if str in dictionary:
        dictionary[str] = dictionary[str] + 1
    else:
        dictionary[str] = 1

print('Start the dictionary iteration')
for key in dictionary:
    print(dictionary[key])
    print(key + ' ')

test = 'Chinese Chinese Chinese Tokyo Japan'
