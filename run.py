import random

# Constants

hangman_images = ['''
    +---+    
    |   |
        |
        |
        |
        |
        |
===========''', '''
    +---+    
    |   |
    O   |
        |
        |
        |
        |
===========''', '''
    +---+    
    |   |
    O   |
    |   |
        |
        |
        |
===========''', '''
    +---+    
    |   |
    O   |
   /|   |
        |
        |
        |
===========''', '''
    +---+    
    |   |
    O   |
   /|\  |
        |
        |
        |
===========''', '''
    +---+    
    |   |
    O   |
   /|\  |
   /    |
        |
        |
===========''', '''
    +---+    
    |   |
    O   |
   /|\  |
   / \  |
        |
        |
===========''']


secretWord = random.choice(words)


def function greeting():

# Welcome messages
name = input ('Welcome to Hangman. Please enter your player name:' )
if name.isalpha():
    print("Hello " + name + " it's nice to meet you" + "!")
    print('Welcome to Hangman. Ready to swing?')
elif name.isdigit():
    print('Sorry, you can only to use letters only to spell your player name! Try again')
else:
    print('You cannot use any special characters in player name.')

correct = []
incorrect = []
failCount = 6
lettersGuessed = " "


while failCount > 0:

    print('===============================')

    guess = input('Please enter a letter:')

    if guess in secretWord:
        correct.append(guess)
        print(f"Correct! There is one or more {guess} in the secretWord")
    else:
        failCount -= 1
        incorrect.append(guess)
        print(f"Incorrect! There is no {guess} in the answer.")
    
    lettersGuessed = lettersGuessed + guess




    def displayBoard(hangman_images, incorrect, correct, secretWord):
        print(hangman_images[len(incorrect)])
    print()

    print('Missed Letters:', end=' ')
    for letter in incorrect:
        print(letter, end=' ')
    print("\n")

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):  # replace blanks with correctly guessed letters
        if secretWord[i] in correct:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:  # show the secret word with spaces in between each letter
        print(letter, end=' ')
    print("\n")

    

    
    

