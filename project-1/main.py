# constant to append and prepend
prepend = '<s>'
append = '</s>'

# TRAIN file
# store all the strings from reading the files
container = []

# reading from the file
openFile = open('brown-train.txt', 'r')
openRead = openFile.readlines()

for currentLine in openRead:
    # print(currentLine)
    currentLine = currentLine.lower()  # lowecase everything
    lastIndex = len(currentLine) - 1
    currentLine = currentLine[:lastIndex] + " " + \
        append + " " + currentLine[lastIndex:]
    container.append(prepend + " " + currentLine)
openFile.close()

# writing to the file
bt = open("brown-train-after.txt", "w")
for a in container:
    bt.write(a)
bt.close()

# DICTIONARY
d = dict()  # dictionary

openFile = open('brown-train-after.txt', 'r')
openRead = openFile.readlines()

for currentLine in openRead:
    for oneString in currentLine.split(" "):
        if oneString in d:
            d[oneString] += 1
        else:
            d[oneString] = 1

for k, v in d.items():
    print(k, v)

# NEXT FILE
container = []

# reading from the file
openFile = open('brown-test.txt', 'r')
openRead = openFile.readlines()

for currentLine in openRead:
    # print(currentLine)
    currentLine = currentLine.lower()  # lowecase everything
    lastIndex = len(currentLine) - 1
    currentLine = currentLine[:lastIndex] + " " + \
        append + " " + currentLine[lastIndex:]
    container.append(prepend + " " + currentLine)
openFile.close()

# writing to the file
bt = open("brown-test-after.txt", "w")
for a in container:
    bt.write(a)
bt.close()

# NEXT FILE: LEARNER-TEST
container = []

# reading from the file
openFile = open('learner-test.txt', 'r')
openRead = openFile.readlines()

for currentLine in openRead:
    # print(currentLine)
    currentLine = currentLine.lower()  # lowecase everything
    lastIndex = len(currentLine) - 1
    currentLine = currentLine[:lastIndex] + " " + \
        append + " " + currentLine[lastIndex:]
    container.append(prepend + " " + currentLine)
openFile.close()

# writing to the file
bt = open("learner-test-after.txt", "w")
for a in container:
    bt.write(a)
bt.close()
