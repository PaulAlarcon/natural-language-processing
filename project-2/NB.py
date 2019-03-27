# take training file, test file, file where the parameters of the resulting model will be saved, and the result itself in own file.
# last line in output file should list the overall accuracy of the classifier on test data
# training and test should've this format: one ex per line, each line corresponds to one example
# first column is the label, other column are feature value
from __future__ import division

# start answer for movie-review-small
sentences_all = []

with open('movie-review-small.NB', 'r') as movie_review_text:
    for line in movie_review_text:
        current_sentence = line[:-1]
        sentences_all.append(current_sentence)

movie_review_small_action = []
movie_review_small_comedy = []
dict_action = {}
dict_comedy = {}
dict_both = {}
count_comedy_sentence = 0
count_action_sentence = 0

for sentence in sentences_all:
    sentence_splitted = sentence.split(',')

    if sentence_splitted[0] == 'comedy':
        count_comedy_sentence = count_comedy_sentence + 1

        for feature in sentence_splitted[1].split(" "):
            movie_review_small_comedy.append(feature)

            if feature in dict_comedy.keys():
                dict_comedy[feature] = dict_comedy[feature] + 1
            else:
                dict_comedy[feature] = 1

            if feature not in dict_both.keys():
                dict_both[feature] = feature
    else:
        count_action_sentence = count_action_sentence + 1

        for feature in sentence_splitted[1].split(" "):
            movie_review_small_action.append(feature)

            if feature in dict_action.keys():
                dict_action[feature] = dict_action[feature] + 1
            else:
                dict_action[feature] = 1

            if feature not in dict_both.keys():
                dict_both[feature] = feature

size_dict_action = sum(dict_action.values())
size_dict_comedy = sum(dict_comedy.values())
size_vocab = len(dict_both)

output = open('movie-review-small-output-parameter.txt', 'w+')

# calculating probabilities for the dictionary
dict_answer = {}
for key in dict_both.keys():
    string = 'P(' + key + '|action)'
    if key not in dict_action.keys():
        calculation = 1 / (size_dict_action + size_vocab)
    else:
        calculation = (dict_action[key] + 1)/(size_dict_action + size_vocab)

    dict_answer[string] = calculation

    string = string + ' = ' + str(calculation)
    output.write(string + '\n')

for key in dict_both.keys():
    string = 'P(' + key + '|comedy)'
    if key not in dict_comedy.keys():
        calculation = 1 / (size_dict_comedy + size_vocab)
    else:
        calculation = (dict_comedy[key] + 1)/(size_dict_comedy + size_vocab)

    dict_answer[string] = calculation

    string = string + ' = ' + str(calculation)
    output.write(string + '\n')

string = 'P(action)'
calculationAction = count_action_sentence / \
    (count_action_sentence + count_comedy_sentence)
dict_answer[string] = calculationAction

string = string + ' = ' + str(calculationAction)
output.write(string + '\n')

string = 'P(comedy)'
calculationComedy = count_comedy_sentence / \
    (count_action_sentence + count_comedy_sentence)
dict_answer[string] = calculationComedy
string = string + ' = ' + str(calculationComedy)
output.write(string + '\n')
print(dict_answer)

test = ['fast', 'couple', 'shoot', 'fly']

probabilityAction = dict_answer['P(action)']
print(probabilityAction)
for string in test:
    key = 'P(' + string + '|action)'
    print(key)
    print(dict_answer[key])
    probabilityAction = probabilityAction * dict_answer[key]

print(probabilityAction)
output.write('P(fast, couple, shoot, fly | action) = ' +
             str(probabilityAction) + '\n')

probabilityComedy = dict_answer['P(comedy)']
print(probabilityComedy)
for string in test:
    key = 'P(' + string + '|comedy)'
    print(key)
    print(dict_answer[key])
    probabilityComedy = probabilityComedy * dict_answer[key]

print(probabilityComedy)
output.write('P(fast, couple, shoot, fly | comedy) = ' +
             str(probabilityComedy) + '\n')


def notused():
    fAction = open('movie-review-small-action.txt', 'w+')
    fComedy = open('movie-review-small-comedy.txt', 'w+')

    for string in sentences_all:
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
            if eachItem in dictComedy.keys():
                dictComedy[eachItem] = dictComedy[eachItem] + 1
            else:
                dictComedy[eachItem] = 1

# print('Dictionary in action')
# print(dictAction)
# print('Dictionary in comedy')
# print(dictComedy)


def NB(trainingFile, testFile, fileParameter, outputFile):
    print('Naive Bayes Algorithm')
