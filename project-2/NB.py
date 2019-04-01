import math

def NB(training_file, test_file, parameter_file, result_file):
    sentences_all = []
    label = []
    createSentencesAndLabel(training_file, sentences_all, label)

    dict_first_label = {}
    dict_second_label = {}
    my_vocab = createVocab()
    createDict(sentences_all, label, dict_first_label, dict_second_label, my_vocab)

    count_first_label_sentence = countSentence(sentences_all, label[0])
    count_second_label_sentence = countSentence(sentences_all, label[1])

    dict_answer = {}
    writeParameter(parameter_file, dict_first_label, dict_second_label, my_vocab, label, dict_answer, count_first_label_sentence, count_second_label_sentence)
    writeResult(test_file, result_file, label, dict_answer)
    writeAccuracy(result_file)

def NB_test(training_file, test_file, parameter_file, result_file):
    sentences_all = []
    label = []
    createSentencesAndLabel(training_file, sentences_all, label)

    dict_first_label = {}
    dict_second_label = {}
    dict_both = {}

    for sentence in sentences_all:
        sentence_splitted = sentence.split(",", 1)
        if sentence_splitted[0] == label[0]:
            for feature in sentence_splitted[1].split(" "):
                if feature == '':
                    continue
                if feature in dict_first_label.keys():
                    dict_first_label[feature] = dict_first_label[feature] + 1
                else:
                    dict_first_label[feature] = 1

                if feature in dict_both.keys():
                    dict_both[feature] = dict_both[feature] + 1
                else:
                    dict_both[feature] = 1
        else:
            for feature in sentence_splitted[1].split(" "):
                if feature == '':
                    continue
                if feature in dict_second_label.keys():
                    dict_second_label[feature] = dict_second_label[feature] + 1
                else:
                    dict_second_label[feature] = 1

                if feature in dict_both.keys():
                    dict_both[feature] = dict_both[feature] + 1
                else:
                    dict_both[feature] = 1
        

    count_first_label_sentence = countSentence(sentences_all, label[0])
    count_second_label_sentence = countSentence(sentences_all, label[1])

    dict_answer = {}
    writeParameter(parameter_file, dict_first_label, dict_second_label, dict_both, label, dict_answer, count_first_label_sentence, count_second_label_sentence)

    test_reader = open(test_file, 'r+', encoding="utf8")
    result_file_reader = open(result_file, 'w+', encoding="utf8")

    for sentence in test_reader:
        sentence_splitted = sentence.split(" ")
        answer_dict = {}
        for each_label in label:
            answer = 'P('
            string = 'P(' + each_label + ')'
            probability_answer = dict_answer[string]
            
            for item in sentence_splitted:
                if item == "\n" or item == '':
                    continue

                key = 'P(' + item + '|' + each_label + ')'

                if key not in dict_answer:
                    continue

                answer = answer + item
                probability_answer = probability_answer * dict_answer[key]

            answer = answer + '|' + each_label + ') = '
            answer_dict[each_label] = probability_answer

            result_file_reader.write(answer + str(probability_answer) + ' \n')

        if answer_dict[label[0]] >= answer_dict[label[1]]:
            result_file_reader.write(label[0] + ', ' + sentence)
        else:
            result_file_reader.write(label[1] + ', ' + sentence)
    result_file_reader.close()

def createVocab():
    my_dict = {}

    vocab_file = open('./movie-review-HW2/aclImdb/imdb.vocab', encoding="utf8")
    for word in vocab_file:
        word_without_newline = word[:-1]
        my_dict[word_without_newline] = 1
    vocab_file.close()

    return my_dict

def createSentencesAndLabel(training_file, sentences_all, label):
    training_file_open = open(training_file, 'r', encoding="utf8")

    for line in training_file_open:
        current_sentence = line[:-1]
        sentences_all.append(current_sentence)

        splitted_sentence = current_sentence.split(",", 1)
        if splitted_sentence[0] not in label:
            label.append(splitted_sentence[0])
    return

def createDict(sentences_all, label, dict_first_label, dict_second_label, my_vocab):
    for sentence in sentences_all:
        sentence_splitted = sentence.split(",", 1)
        if sentence_splitted[0] == label[0]:
            for feature in sentence_splitted[1].split(" "):
                if feature not in my_vocab.keys():
                    continue

                if feature in dict_first_label.keys():
                    dict_first_label[feature] = dict_first_label[feature] + 1
                    continue

                if feature in my_vocab.keys():
                    dict_first_label[feature] = my_vocab[feature]
        else:
            for feature in sentence_splitted[1].split(" "):
                if feature not in my_vocab.keys():
                    continue

                if feature in dict_second_label.keys():
                    dict_second_label[feature] = dict_second_label[feature] + 1
                    continue

                if feature in my_vocab.keys():
                    dict_second_label[feature] = my_vocab[feature]
    return

def countSentence(sentences_all, label):
    count = 0
    for sentence in sentences_all:
        sentence_splitted = sentence.split(',')
        if sentence_splitted[0] == label:
            count = count + 1
    return count

def writeParameter(parameter_file, dict_first_label, dict_second_label, my_vocab, label, dict_answer, count_first_label_sentence, count_second_label_sentence):
    parameter_output = open(parameter_file, 'w+', encoding="utf8")

    size_dict_first_label = sum(dict_first_label.values())
    size_dict_second_label = sum(dict_second_label.values())
    size_vocab = len(my_vocab)

    for key in my_vocab.keys():
        parameter_first_label = 'P(' + key + '|' + label[0] + ')'
        if key not in dict_first_label.keys():
            calculation = 1 / (size_dict_first_label + size_vocab)
        else:
            calculation = (dict_first_label[key] + 1) / (size_dict_first_label + size_vocab)

        dict_answer[parameter_first_label] = calculation

        parameter_first_label = parameter_first_label + ' = ' + str(calculation)
        parameter_output.write(parameter_first_label + '\n')

        parameter_second_label = 'P(' + key + '|' + label[1] + ')'
        if key not in dict_second_label.keys():
            calculation = 1 / (size_dict_second_label + size_vocab)
        else:
            calculation = (dict_second_label[key] + 1) / (size_dict_second_label + size_vocab)

        dict_answer[parameter_second_label] = calculation

        parameter_second_label = parameter_second_label + ' = ' + str(calculation)
        parameter_output.write(parameter_second_label + '\n')
    
    parameter_first_label = 'P(' + label[0] + ')'
    calculation = count_first_label_sentence / (count_second_label_sentence + count_first_label_sentence)
    dict_answer[parameter_first_label] = calculation

    parameter_first_label = parameter_first_label + ' = ' + str(calculation)
    parameter_output.write(parameter_first_label + '\n')

    second_label = 'P(' + label[1] + ')'
    calculation = count_second_label_sentence / (count_second_label_sentence + count_first_label_sentence)
    dict_answer[second_label] = calculation

    second_label = second_label + ' = ' + str(calculation)
    parameter_output.write(second_label + '\n')

def writeResult(test_file, result_file, label, dict_answer):
    test_reader = open(test_file, 'r+', encoding="utf8")
    result_file_reader = open(result_file, 'w+', encoding="utf8")

    for sentence in test_reader:
        sentence_splitted = sentence.split(" ")
        answer_dict = {}
        for each_label in label:
            answer = 'P('
            string = 'P(' + each_label + ')'
            probability_answer = math.log(dict_answer[string], 2)
            
            for item in sentence_splitted:
                if item == "\n" or item == '':
                    continue

                key = 'P(' + item + '|' + each_label + ')'

                if key not in dict_answer:
                    continue

                answer = answer + item
                probability_answer = probability_answer + math.log(dict_answer[key], 2)

            answer = answer + '|' + each_label + ') = '
            answer_dict[each_label] = probability_answer

        if answer_dict[label[0]] >= answer_dict[label[1]]:
            result_file_reader.write(label[0] + ', ' + sentence)
        else:
            result_file_reader.write(label[1] + ', ' + sentence)
    result_file_reader.close()

def writeAccuracy(result_file):
    result_file_reader = open(result_file, 'r+', encoding="utf8")
    check_file = open('check-test-document.txt', 'r+', encoding="utf8")
    
    count_mismatch = 0
    count_accurate = 0
    count_total = 0

    for sentence in result_file_reader:
        sentence_splitted = sentence.split(",", 1)
        
        sentence_test = check_file.readline()
        sentence_test_splitted = sentence_test.split(",", 1)

        if sentence_splitted[0] == sentence_test_splitted[0]:
            count_accurate = count_accurate + 1
        else:
            count_mismatch = count_mismatch + 1

        count_total = count_total + 1
    result_file_reader.write('Total prediction correct: ' + str(count_accurate) + '\n')
    result_file_reader.write('Total prediction missmatch: ' + str(count_mismatch) + '\n')
    result_file_reader.write('Total prediction being made: ' + str(count_total) + '\n')
    result_file_reader.write('How accurate is my algorithm ' + str(count_accurate/count_total) + '\n')

NB_test('movie-review-small-training.txt','movie-review-small-test.txt', 'movie-review-small.NB', 'movie-review-small-output.txt')

NB('movie-review-combined-training.txt', 'movie-review-combined-test.txt','movie-review-BOW.NB', 'movie-review-combined-output.txt')
