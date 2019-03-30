# take training / test directory containing movie review.
# perform pre-processing on each file and output files in the vector format to be used by NB.py

# separate punctuation from words, lowercase words in reviews.
# BOW = bag of words
import os
import re

my_working_dir = os.getcwd()

one_big_training_document = open('movie-review-combined-training.txt', 'w+')
one_big_test_document = open('movie-review-combined-test.txt', 'w+')


def combineTrainingReview(my_working_dir, directory, class_file, label):
    os.chdir(directory)
    all_files_inside_dir = os.listdir(".")

    container_word_in_review = []
    container_sentence_in_review = []

    for each_file in all_files_inside_dir:
        f = open(each_file, 'r+')
        sentence = f.readline()

        review_lower = sentence.lower()
        list_review_removed_punctuation = re.findall(
            r"[\w']+|[.,!?;]", review_lower)

        sentence = " "
        sentence = sentence.join(list_review_removed_punctuation)

        container_sentence_in_review.append(sentence)

        for word in list_review_removed_punctuation:
            container_word_in_review.append(word)
        f.close()

    os.chdir(my_working_dir)
    vocab_file = open('movie-review-' + class_file + '.vocab', 'w+')
    for word in container_word_in_review:
        vocab_file.write(word + ' \n')
    vocab_file.close()

    for sentence in container_sentence_in_review:
        one_big_training_document.write(label + sentence + ' \n')


def combineTestReview(my_working_dir, directory, class_file):
    os.chdir(directory)
    all_files_inside_dir = os.listdir(".")
    container_review = []

    for each_file in all_files_inside_dir:
        f = open(each_file, 'r+')
        for sentence in f:
            review_lower = sentence.lower()
            list_review_removed_punctuation = re.findall(
                r"[\w']+|[.,!?;]", review_lower)

            sentence_after_removed_punctuation = ''
            for string in list_review_removed_punctuation:
                sentence_after_removed_punctuation = sentence_after_removed_punctuation + ' ' + string
            sentence_after_removed_punctuation = sentence_after_removed_punctuation.strip()

            container_review.append(sentence_after_removed_punctuation)
        f.close()

    os.chdir(my_working_dir)
    f = open('movie-review-' + class_file + '-testing.txt', 'w+')
    for sentence in container_review:
        f.write(sentence + ' \n')
        one_big_test_document.write(sentence + ' \n')
    f.close()


combineTrainingReview(my_working_dir,
                      'movie-review-HW2/aclImdb/train/pos', 'positive', '+,')

combineTrainingReview(my_working_dir,
                      'movie-review-HW2/aclImdb/train/neg', 'negative', '-,')

combineTestReview(
    my_working_dir, 'movie-review-HW2/aclImdb/test/pos', 'positive')

combineTestReview(
    my_working_dir, 'movie-review-HW2/aclImdb/test/neg', 'negative')
