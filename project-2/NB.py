# take training file, test file, file where the parameters of the resulting model will be saved, and the result itself in own file.
# last line in output file should list the overall accuracy of the classifier on test data
# training and test should've this format: one ex per line, each line corresponds to one example
# first column is the label, other column are feature value
from __future__ import division


def NB(training_file, test_file, parameter_file, result_file):
    sentences_all = []
    label = []

    with open(training_file, 'r') as training_file_open:
        for line in training_file_open:
            current_sentence = line[:-1]
            splitted_sentence = current_sentence.split(",")
            if splitted_sentence[0] not in label:
                label.append(splitted_sentence[0])
            sentences_all.append(current_sentence)

    dict_first_label = {}
    dict_second_label = {}
    dict_both = {}

    count_first_label_sentence = 0
    count_second_label_sentence = 0

    # creating dictionary for both label
    # storing each unique values in both label
    # counting how many sentences in both label
    for sentence in sentences_all:
        sentence_splitted = sentence.split(',')

        if sentence_splitted[0] == label[0]:
            count_first_label_sentence = count_first_label_sentence + 1

            for feature in sentence_splitted[1].split(" "):
                if feature in dict_first_label.keys():
                    dict_first_label[feature] = dict_first_label[feature] + 1
                else:
                    dict_first_label[feature] = 1

                if feature not in dict_both.keys():
                    dict_both[feature] = feature
        else:
            count_second_label_sentence = count_second_label_sentence + 1

            for feature in sentence_splitted[1].split(" "):
                if feature in dict_second_label.keys():
                    dict_second_label[feature] = dict_second_label[feature] + 1
                else:
                    dict_second_label[feature] = 1

                if feature not in dict_both.keys():
                    dict_both[feature] = feature

    size_dict_second_label = sum(dict_second_label.values())
    size_dict_first_label = sum(dict_first_label.values())
    size_vocab = len(dict_both)

    # calculating parameters and storing it inside the parameter file
    parameter_output = open(parameter_file, 'w+')
    dict_answer = {}
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

    string = 'P(action)'
    calculationAction = count_second_label_sentence / \
        (count_second_label_sentence + count_first_label_sentence)
    dict_answer[string] = calculationAction

    string = string + ' = ' + str(calculationAction)
    parameter_output.write(string + '\n')

    string = 'P(comedy)'
    calculationComedy = count_first_label_sentence / \
        (count_second_label_sentence + count_first_label_sentence)
    dict_answer[string] = calculationComedy
    string = string + ' = ' + str(calculationComedy)
    parameter_output.write(string + '\n')
    print(dict_answer)
    # end of printing parameter

    test_reader = open(test_file, 'r+')
    result_file = open(result_file, 'w+')
    for sentence in test_reader:
        sentence_splitted = sentence.split(" ")
        for each_label in label:
            answer = 'P('
            string = 'P(' + each_label + ')'
            probability_answer = dict_answer[string]
            for item in sentence_splitted:
                if item == "\n":
                    continue
                key = 'P(' + item + '|' + each_label + ')'
                answer = answer + item
                print(key)
                probability_answer = probability_answer * dict_answer[key]

            answer = answer + '|' + each_label + ') = '
            result_file.write(answer + str(probability_answer) + '\n')


NB('movie-review-small-training.txt',
   'movie-review-small-test.txt', 'movie-review-small.NB', 'movie-review-small-output.txt')
