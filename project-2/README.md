#How to run the program:

You need to download the data set and the testing set from this link:
https://drive.google.com/file/d/1HuIT9KOGmTQH7NJGF5qcOXwSooQg5UBc/view

In this project, I practice Naive Bayes algorithm by taking set of data and then using supervised learning, my program will learn to detect if a sentence, in this case, is a review, will be tagged as a positive or negative review. 

Using the link above, you will get training set and testing set. I combined training set into one big document and tag them with their respective label. I also combined the testing set into one big document. 

Utilizing bag-of-words, and also conditional probability, I would get the probability of each sentence/review in the test folder as a positive or negative reviews. In the end, I would use the maximum probability and would label them. So if p(sentence|positive review) > p(sentence|negative review) I would assign that review with positive review