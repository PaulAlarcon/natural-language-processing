import os
import re


def positiveReview():
    # use this to refer to my original working directory
    myWorkingDirectory = os.getcwd()

    # change the directory to positive review
    os.chdir('movie-review-HW2/aclImdb/train/pos')

    # get all files inside the negative training. check using print
    filesInsideDirectory = os.listdir(".")

    # contain string to append into new file
    containerForPositiveReviews = []

    # read each files inside the positive folder
    for file in filesInsideDirectory:
        f = open(file, 'r+')

        # read each sentence in the file
        for sentence in f:
            reviewInLower = sentence.lower()

            listReviewRemovedPunctuation = re.findall(
                r"[\w']+|[.,!?;]", reviewInLower)

            sentenceAfterRemovedPunctuation = ''

            for string in listReviewRemovedPunctuation:
                sentenceAfterRemovedPunctuation = sentenceAfterRemovedPunctuation + ' ' + string

            sentenceAfterRemovedPunctuation = sentenceAfterRemovedPunctuation.strip()

            containerForPositiveReviews.append(sentenceAfterRemovedPunctuation)

        f.close()

    # go back to working directory
    os.chdir(myWorkingDirectory)

    f = open('OneBigPositiveReview.txt', 'w+')
    for sentence in containerForPositiveReviews:
        f.write(sentence + ' \n')
    f.close()


def negativeReview():
    # use this to refer to my original working directory
    myWorkingDirectory = os.getcwd()

    # change the directory to negative review
    os.chdir('movie-review-HW2/aclImdb/train/neg')

    # get all files inside the negative training. check using print
    filesInsideDirectory = os.listdir(".")

    # contain string to append into new file
    containerForNegativeReviews = []

    # read each files inside the positive folder
    for file in filesInsideDirectory:
        f = open(file, 'r+')

        # read each sentence in the file
        for sentence in f:
            reviewInLower = sentence.lower()

            listReviewRemovedPunctuation = re.findall(
                r"[\w']+|[.,!?;]", reviewInLower)

            sentenceAfterRemovedPunctuation = ''

            for string in listReviewRemovedPunctuation:
                sentenceAfterRemovedPunctuation = sentenceAfterRemovedPunctuation + ' ' + string

            sentenceAfterRemovedPunctuation = sentenceAfterRemovedPunctuation.strip()

            containerForNegativeReviews.append(sentenceAfterRemovedPunctuation)

    # go back to working directory
    os.chdir(myWorkingDirectory)

    f = open('OneBigNegativeReview.txt', 'w+')
    for sentence in containerForNegativeReviews:
        f.write(sentence + ' \n')


def OneBigJumbleCodeWithExplanation():
    # use this to refer to my original working directory
    myWorkingDirectory = os.getcwd()
    # print(myWorkingDirectory)

    # change the directory to negative review
    os.chdir('movie-review-HW2/aclImdb/train/neg')

    # get all files inside the negative training. check using print
    filesInsideDirectory = os.listdir(".")
    # print(files)

    containerForNegativeReviews = []

    index = 0
    for file in filesInsideDirectory:
        # for testing, stop once reach certain number
        if index == 2:
            break

        # print(file)  # check which file is being opened
        f = open(file, 'r+')

        for sentence in f:
            reviewInLower = sentence.lower()
            listReviewRemovedPunctuation = re.findall(
                r"[\w']+|[.,!?;]", reviewInLower)
            sentenceAfterRemovedPunctuation = ''

            # print('-------begin---- ' + reviewInLower)
            for string in listReviewRemovedPunctuation:
                sentenceAfterRemovedPunctuation = sentenceAfterRemovedPunctuation + ' ' + string
            # print('-------begin---- ' + reviewInLower)
            # print('--after-- ' + sentenceAfterRemovedPunctuation)
            sentenceAfterRemovedPunctuation = sentenceAfterRemovedPunctuation.strip()

            containerForNegativeReviews.append(sentenceAfterRemovedPunctuation)

        index = index + 1

    # go back to working directory
    os.chdir(myWorkingDirectory)
    f = open('smallCode.txt', 'w+')
    for sentence in containerForNegativeReviews:
        f.write(sentence + ' \n')
