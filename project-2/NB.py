# take training file, test file, file where the parameters of the resulting model will be saved, and the result itself in own file.
# last line in output file should list the overall accuracy of the classifier on test data
# training and test should've this format: one ex per line, each line corresponds to one example
# first column is the label, other column are feature value
from __future__ import division
import datetime

my_vocab = {}
vocab_file = open('./movie-review-HW2/aclImdb/imdb.vocab')
for word in vocab_file:
    current_word = word[:-1]
    my_vocab[current_word] = 1

print(my_vocab)


def NB(training_file, test_file, parameter_file, result_file):
    currentDT = datetime.datetime.now()
    print (str(currentDT))

    sentences_all = []
    label = []

    with open(training_file, 'r') as training_file_open:
        for line in training_file_open:
            current_sentence = line[:-1]
            splitted_sentence = current_sentence.split(",", 1)
            # print(splitted_sentence)
            if splitted_sentence[0] not in label:
                label.append(splitted_sentence[0])

            sentences_all.append(current_sentence)

    print('done appending')
    dict_first_label = {}
    dict_second_label = {}
    dict_both = {}
    createDict(sentences_all, label, dict_first_label,
               dict_second_label, dict_both)

    # dict_first_label = createDict2(sentences_all, label[0])
    # print('success creating first dict')

    # dict_second_label = createDict2(sentences_all, label[1])
    # print('success creating second dict')

    # dict_both = createVocab(sentences_all)
    # print('success creating both dict')

    count_first_label_sentence = countSentence(sentences_all, label[0])
    print('success count first label')

    count_second_label_sentence = countSentence(sentences_all, label[1])
    print('success creating second dict')

    parameter_output = open(parameter_file, 'w+')
    dict_answer = {}

    print('begin writing params')
    writeParameter(parameter_output, dict_first_label, dict_second_label, dict_both,
                   label, dict_answer, count_first_label_sentence, count_second_label_sentence)

    # hmm = open('open.txt', 'w+')
    # for key in dict_both.keys():
    #     hmm.write(key + '  ' + str(dict_both[key]) + ' \n')

    # print(dict_answer)
    # print('begin writing result')

    writeResult(test_file, result_file, label, dict_answer)

    currentDT = datetime.datetime.now()
    print (str(currentDT))
    # print(dict_answer)


def createDict(sentences_all, label, dict_first_label, dict_second_label, dict_both):
    index = 0
    for sentence in sentences_all:
        print(index)
        sentence_splitted = sentence.split(",", 1)

        if sentence_splitted[0] == label[0]:
            for feature in sentence_splitted[1].split(" "):
                if feature in dict_first_label.keys():
                    dict_first_label[feature] = dict_first_label[feature] + 1
                else:
                    dict_first_label[feature] = 1

                if feature not in dict_both.keys():
                    dict_both[feature] = 1
        else:
            for feature in sentence_splitted[1].split(" "):
                if feature in dict_second_label.keys():
                    dict_second_label[feature] = dict_second_label[feature] + 1
                else:
                    dict_second_label[feature] = 1

                if feature not in dict_both.keys():
                    dict_both[feature] = feature
        index = index + 1


def createDict2(sentences_all, label):
    my_dict = {}
    for sentence in sentences_all:
        sentence_splitted = sentence.split(",", 1)
        if sentence_splitted[0] == label:
            for feature in sentence_splitted[1].split(" "):
                if feature in my_dict.keys():
                    my_dict[feature] = my_dict[feature] + 1
                else:
                    my_dict[feature] = 1
    return my_dict


def createVocab(sentences_all):
    my_dict = {}
    for sentence in sentences_all:
        sentence_splitted = sentence.split(",", 1)
        print(sentence_splitted)
        for feature in sentence_splitted[1].split(" "):
            if feature not in my_dict.keys():
                my_dict[feature] = 0

    return my_dict


def countSentence(sentences_all, label):
    count = 0
    for sentence in sentences_all:
        sentence_splitted = sentence.split(',')

        if sentence_splitted[0] == label:
            count = count + 1

    return count


def writeParameter(parameter_output, dict_first_label, dict_second_label, dict_both, label, dict_answer, count_first_label_sentence, count_second_label_sentence):
    size_dict_first_label = sum(dict_first_label.values())
    size_dict_second_label = sum(dict_second_label.values())
    size_vocab = len(dict_both)

    for key in dict_both.keys():
        string = 'P(' + key + '|' + label[1] + ')'
        if key not in dict_second_label.keys():
            calculation = 1 / (size_dict_second_label + size_vocab)
        else:
            calculation = (dict_second_label[key] + 1) / \
                (size_dict_second_label + size_vocab)

        dict_answer[string] = calculation

        string = string + ' = ' + str(calculation)
        parameter_output.write(string + '\n')

        string = 'P(' + key + '|' + label[0] + ')'
        if key not in dict_first_label.keys():
            calculation = 1 / (size_dict_first_label + size_vocab)
        else:
            calculation = (dict_first_label[key] + 1) / \
                (size_dict_first_label + size_vocab)

        dict_answer[string] = calculation

        string = string + ' = ' + str(calculation)
        parameter_output.write(string + '\n')

    string = 'P(' + label[1] + ')'
    calculationAction = count_second_label_sentence / \
        (count_second_label_sentence + count_first_label_sentence)
    dict_answer[string] = calculationAction

    string = string + ' = ' + str(calculationAction)
    parameter_output.write(string + '\n')

    string = 'P(' + label[0] + ')'
    calculationComedy = count_first_label_sentence / \
        (count_second_label_sentence + count_first_label_sentence)
    dict_answer[string] = calculationComedy
    string = string + ' = ' + str(calculationComedy)
    parameter_output.write(string + '\n')


def writeResult(test_file, result_file, label, dict_answer):
    test_reader = open(test_file, 'r+')
    result_file = open(result_file, 'w+')
    for sentence in test_reader:
        sentence_splitted = sentence.split(" ")
        answer_dict = {}
        for each_label in label:
            answer = 'P('
            string = 'P(' + each_label + ')'
            probability_answer = dict_answer[string]
            for item in sentence_splitted:
                if item == "\n":
                    continue
                key = 'P(' + item + '|' + each_label + ')'
                answer = answer + item
                probability_answer = probability_answer * dict_answer[key]

            answer = answer + '|' + each_label + ') = '
            answer_dict[each_label] = probability_answer
            result_file.write(answer + str(probability_answer) + '\n')

        if answer_dict[label[0]] > answer_dict[label[1]]:
            result_file.write(label[0] + ', ' + sentence)
        else:
            result_file.write(label[1] + ', ' + sentence)


# NB('movie-review-small-training.txt',
#    'movie-review-small-test.txt', 'movie-review-small.NB', 'movie-review-small-output.txt')

# NB('movie-review-combined-training.txt', 'movie-review-combined-test.txt',
#    'movie-review-combined.NB', 'movie-review-combined-output.txt')
