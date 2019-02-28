import library

print('--Start padding <unk> and </unk> and lowercasing the files respectively--')
library.padSentence()
print('--End of padding <unk> and </unk> and lowercasing the files respectively--')

print('\n--**--**--**--\n')

print('--Start replacing occuring in test file--')
library.replaceOccuring()
print('--End replacing occuring in test file--')


print('\n--**--**--**--\n')

print('Answering questions: ')
library.questionOne()
library.questionTwo()
library.questionThree()
