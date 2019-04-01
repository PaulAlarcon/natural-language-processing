import os
import re

my_working_dir = os.getcwd()

one_big_training_document = open('movie-review-combined-training.txt', 'w+', encoding="utf8")
one_big_test_document = open('movie-review-combined-test.txt', 'w+', encoding="utf8")
check_test_document = open('check-test-document.txt', 'w+', encoding="utf8")

def combineTrainingReview(my_working_dir, directory, class_file, label):
    os.chdir(directory)

    all_files_inside_dir = os.listdir(".")
    container_review = []

    for each_file in all_files_inside_dir:
        each_file_open = open(each_file, 'r+', encoding="utf8")

        sentence =  each_file_open.readline()
        review_lower = sentence.lower()
        list_review_removed_punctuation = re.findall(r"[\w']+|[.,!?;]", review_lower)

        sentence = " "
        sentence = sentence.join(list_review_removed_punctuation).strip()
        container_review.append(sentence)

        each_file_open.close()

    os.chdir(my_working_dir)
    review_training_file = open('movie-review-' + class_file + '-training.txt', 'w+', encoding="utf8")
    for sentence in container_review:
        review_training_file.write(label + sentence + ' \n')
        one_big_training_document.write(label + sentence + ' \n')
    review_training_file.close()


def combineTestReview(my_working_dir, directory, class_file, label):
    os.chdir(directory)

    all_files_inside_dir = os.listdir(".")
    container_review = []

    for each_file in all_files_inside_dir:
        each_file_open = open(each_file, 'r+', encoding="utf8")

        sentence = each_file_open.readline()
        review_lower = sentence.lower()
        list_review_removed_punctuation = re.findall(r"[\w']+|[.,!?;]", review_lower)

        sentence = " "
        sentence = sentence.join(list_review_removed_punctuation).strip()
        container_review.append(sentence)

        each_file_open.close()

    os.chdir(my_working_dir)
    review_test_file = open('movie-review-' + class_file + '-testing.txt', 'w+', encoding="utf8")
    for sentence in container_review:
        review_test_file.write(sentence + ' \n')
        one_big_test_document.write(sentence + ' \n')
        check_test_document.write(label + ' ' + sentence + ' \n')
    review_test_file.close()


combineTrainingReview(my_working_dir,'movie-review-HW2/aclImdb/train/pos','positive','+,')
combineTrainingReview(my_working_dir,'movie-review-HW2/aclImdb/train/neg','negative','-,')

combineTestReview(my_working_dir,'movie-review-HW2/aclImdb/test/pos','positive', '+,')
combineTestReview(my_working_dir,'movie-review-HW2/aclImdb/test/neg','negative', '-,')
