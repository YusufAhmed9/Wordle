wordList = []
with open('Words.txt', 'r') as file:
    for line in file:
        word = line.strip()
        wordList.append(word)