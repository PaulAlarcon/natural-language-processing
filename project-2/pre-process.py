# take training / test directory containing movie review.
# perform pre-processing on each file and output files in the vector format to be used by NB.py

# separate punctuation from words, lowercase words in reviews.
# BOW = bag of words
import os
import re
import preprocessLibrary

# preprocessLibrary.positiveReview()
# preprocessLibrary.negativeReview()

# preprocessLibrary.OneBigJumbleCodeWithExplanation()
# preprocessLibrary.DictionaryTest()

negativeReviewDict = preprocessLibrary.createNegativeDict()
numWordInNegativeReview = sum(negativeReviewDict.values())
print(numWordInNegativeReview)

positiveReviewDict = preprocessLibrary.createPositiveDict()
numWordInPositiveReview = sum(positiveReviewDict.values())
print(numWordInPositiveReview)
