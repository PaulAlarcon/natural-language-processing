# take training / test directory containing movie review.
# perform pre-processing on each file and output files in the vector format to be used by NB.py

# separate punctuation from words, lowercase words in reviews.
# BOW = bag of words
import os
import re
import nltk
nltk.download()


# data = "All work and no play makes jack a dull boy, all work and no play"
# print(word_tokenize(data))

print(re.findall(r"[\w']+|[.,!?;]", "Words, words, words."))
print(re.findall(r"[\w']+|[.,!?;]", "I'm"))
print(re.findall(r"[\w']+|[.,!?;]", "U.S.A"))

# get the directory inside of train negative files
filesInsideTrainingNegDirectory = os.listdir(
    'movie-review-HW2/aclImdb')
print(filesInsideTrainingNegDirectory)

# IGNORE UP

# use this to refer to my original working directory
myWorkingDirectory = os.getcwd()
print(myWorkingDirectory)

# change the directory to negative review
os.chdir('movie-review-HW2/aclImdb/train/neg')

filesInsideDirectory = os.listdir(".")  # get all files inside the directory
# print(files)

containerForNegativeReviews = []
index = 0

for file in filesInsideDirectory:
    if index == 3:
        break

    print(file)  # check which file is being opened
    f = open(file, 'r+')

    for sentence in f:
        reviewInLower = sentence.lower()
        print('-------begin---- ' + reviewInLower)
        containerForNegativeReviews.append(reviewInLower)

    index = index + 1

# go back to working directory
os.chdir(myWorkingDirectory)

f = open('negativeReview.txt', 'w+')

for sentence in containerForNegativeReviews:
    f.write(sentence + '\n')
