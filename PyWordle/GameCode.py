import GameWords
import random
from collections import defaultdict

def StartMenu():
    print("1. Start game")
    print("2. Instructions")
    print("3. Close game")
    choice = int(input())
    return choice

def getGame():
    systemWord = random.choice(GameWords.wordList)
    lettersLeft = defaultdict(int)
    for letter in systemWord:
        lettersLeft[letter] += 1
    guessesLimit = 6
    while guessesLimit > 0:
        guessLettersLeft = lettersLeft.copy()
        print("Enter a word:", end = ' ')
        
        word = input()
        while (word in GameWords.wordList) == False:
            print("Word not found")
            word = input()

        guess = ''
        for index, letter in enumerate(word):
            if letter == systemWord[index] and guessLettersLeft[letter]:
                guess += '!'
                guessLettersLeft[letter] -= 1
            
            elif letter in systemWord and guessLettersLeft[letter]:
                guess += '?'
                guessLettersLeft[letter] -= 1
           
            else:
                guess += '*'
        if guess.count('!') == len(guess):
            print("Nice !")
            break
        
        else:
            print(guess)
        
        guessesLimit -= 1
    print("The word is " + systemWord)

def instructionsList():
    data = '''
    Rules:
    If the letter is in its correct place : !
    If the letter exists in the word      : ?
    If the letter is not in the word      : *
'''
    print(data)


while True:
    currentChoice = StartMenu()
#-------------------------------------
    if currentChoice == 1:
        getGame()

#-------------------------------------
    elif currentChoice == 2:
        instructionsList()

#-------------------------------------
    else:
        break