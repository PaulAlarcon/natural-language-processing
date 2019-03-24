import os
import re


def negativeReview():
    # use this to refer to my original working directory
    myWorkingDirectory = os.getcwd()
    print(myWorkingDirectory)

    # change the directory to negative review
    os.chdir('movie-review-HW2/aclImdb/train/neg')

    # get all files inside the negative training. check using print
    filesInsideDirectory = os.listdir(".")
    # print(files)

    containerForNegativeReviews = []

    # index = 0

    for file in filesInsideDirectory:
        # for testing, stop once reach certain number
        # if index == 15:
        #     break

        print(file)  # check which file is being opened
        f = open(file, 'r+')

        for sentence in f:
            reviewInLower = sentence.lower()
            listReviewRemovedPunctuation = re.findall(
                r"[\w']+|[.,!?;]", reviewInLower)
            sentenceAfterRemovedPunctuation = ''

            print('-------begin---- ' + reviewInLower)
            for string in listReviewRemovedPunctuation:
                sentenceAfterRemovedPunctuation = sentenceAfterRemovedPunctuation + ' ' + string
            print('-------begin---- ' + reviewInLower)
            print('--after-- ' + sentenceAfterRemovedPunctuation)

            containerForNegativeReviews.append(sentenceAfterRemovedPunctuation)

        # index = index + 1

    # go back to working directory
    os.chdir(myWorkingDirectory)
    f = open('OneBigNegativeReview.txt', 'w+')
    for sentence in containerForNegativeReviews:
        f.write(sentence + '\n')


def oneBigJumbleCode():
    # get the directory inside of train negative files
    filesInsideTrainingNegDirectory = os.listdir(
        'movie-review-HW2/aclImdb')
    print(filesInsideTrainingNegDirectory)

    # use this to refer to my original working directory
    myWorkingDirectory = os.getcwd()
    print(myWorkingDirectory)

    # change the directory to negative review
    os.chdir('movie-review-HW2/aclImdb/train/neg')

    # get all files inside the directory
    filesInsideDirectory = os.listdir(".")
    # print(files)

    containerForNegativeReviews = []
    # index = 0

    for file in filesInsideDirectory:
        # for testing, stop once reach certain number
        # if index == 15:
        #     break

        print(file)  # check which file is being opened
        f = open(file, 'r+')

        for sentence in f:
            reviewInLower = sentence.lower()
            reviewRemovedPunctuation = re.findall(
                r"[\w']+|[.,!?;]", reviewInLower)
            sentenceAfterRemovedPunctuation = ''

            print('-------begin---- ' + reviewInLower)
            for string in reviewRemovedPunctuation:
                sentenceAfterRemovedPunctuation = sentenceAfterRemovedPunctuation + ' ' + string
            print('-------begin---- ' + reviewInLower)
            print('--after-- ' + sentenceAfterRemovedPunctuation)

            containerForNegativeReviews.append(sentenceAfterRemovedPunctuation)

        # index = index + 1

    # go back to working directory
    os.chdir(myWorkingDirectory)

    f = open('OneBigNegativeReview.txt', 'w+')

    for sentence in containerForNegativeReviews:
        f.write(sentence + '\n')
