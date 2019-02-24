def paddingSentence(url):
    # constant to append and prepend
    prepend = '<s>'
    append = '</s>'

    # store all the strings from reading the files
    container = []

    # reading from the file
    openFile = open(url + '.txt', 'r')
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
    bt = open(url + "-after.txt", "w")
    for a in container:
        bt.write(a)
    bt.close()


def createDictionary():
    d = dict()  # my dictionary

    openFile = open('brown-train-after.txt', 'r')
    openRead = openFile.readlines()

    for currentLine in openRead:
        for oneString in currentLine.split(" "):
            if oneString in d:
                d[oneString] += 1
            else:
                d[oneString] = 1

    # for k, v in d.items():
    #     print(k, v)

    f = open("dict.txt", "w")
    f.write(str(d))
    f.close


def replaceOccuringWord():
    d = dict()  # my dictionary

    openFile = open('brown-train-after.txt', 'r')
    openRead = openFile.readlines()

    for currentLine in openRead:
        for oneString in currentLine.split(" "):
            if oneString in d:
                d[oneString] += 1
            else:
                d[oneString] = 1

    # REPLACE ALL WORD OCCURING IN TRAINING DATA ONCE WITH THE TOKEN UNK
    # reading from the file
    openFile = open('brown-train-after.txt', 'r')
    openRead = openFile.readlines()

    container = []

    # REPLACE THE WORD WITH UNKNOWN
    for currentLine in openRead:
        # print(currentLine)
        txt = ""
        currentLine = currentLine.lower()  # lowecase everything
        for oneString in currentLine.split(" "):
            if d.get(oneString) == 1:
                txt = txt + " <unk>"
            else:
                txt = txt + " " + oneString
        container.append(currentLine)
    openFile.close()

    # writing to the file
    bt = open("brown-train-after-replaced-unk.txt", "w")
    for string in container:
        bt.write(string)
    bt.close()

    # ----------
    # REPLACE ALL WORD NOT OCCURING IN BROWN-TEST DATA ONCE WITH THE TOKEN UNK
    # reading from the file
    openFile = open('brown-test-after.txt', 'r')
    openRead = openFile.readlines()

    container = []

    # REPLACE THE WORD WITH UNKNOWN
    for currentLine in openRead:
        # print(currentLine)
        txt = ""
        currentLine = currentLine.lower()  # lowecase everything
        for key in currentLine.split(" "):
            if key not in d.keys():
                txt = txt + " <unk>"
            else:
                # print("appear " + key)
                txt = txt + " " + key

        # print(txt)
        container.append(txt)
    openFile.close()

    # writing to the file
    bt = open("brown-test-after-replaced-unk.txt", "w")
    for string in container:
        bt.write(string)
    bt.close()

    # ----------
    # REPLACE ALL WORD NOT OCCURING IN LEARNER-TEST DATA ONCE WITH THE TOKEN UNK
    # reading from the file
    openFile = open('learner-test-after.txt', 'r')
    openRead = openFile.readlines()

    container = []

    # REPLACE THE WORD WITH UNKNOWN
    for currentLine in openRead:
        # print(currentLine)
        txt = ""
        currentLine = currentLine.lower()  # lowecase everything
        for key in currentLine.split(" "):
            if key not in d.keys():
                txt = txt + " <unk>"
            else:
                # print("appear " + key)
                txt = txt + " " + key

        # print(txt)
        container.append(txt)
    openFile.close()

    # writing to the file
    bt = open("learner-test-after-replaced-unk.txt", "w")
    for string in container:
        bt.write(string)
    bt.close()


paddingSentence('brown-train')  # padding the brown-train file
paddingSentence('learner-test')  # padding the learner-test file
paddingSentence('brown-test')  # padding the brown-test file

createDictionary()

replaceOccuringWord()
