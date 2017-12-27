# Hangman

import random
import string

# Add complete path name if IOError eg. "F:/Projects/Hangman/words.txt"
WORDLIST_FILENAME = "words.txt"


def loadWords():

    """
    Returns a list of valid words. Words are strings of lowercase letters.
    """

    print("Loading word list from file...")

    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')

    # line: string
    line = inFile.readline()

    # wordlist: list of strings
    wordlist = line.split()

    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):

    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """

    return random.choice(wordlist)


def isWordGuessed(secretWord, lettersGuessed):

    """
    secretWord: string, the word the user is guessing

    lettersGuessed: list, what letters have been guessed so far

    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    """

    for i in secretWord:
        if i in lettersGuessed:
            flag = True
        else:
            flag = False
            break
    return flag


def getGuessedWord(secretWord, lettersGuessed):

    """
    secretWord: string, the word the user is guessing

    lettersGuessed: list, what letters have been guessed so far

    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    """

    guessedword = ''
    for i in secretWord:
        if i in lettersGuessed:
            guessedword += i
        else:
            guessedword += ' _'
    return guessedword


def getAvailableLetters(lettersGuessed):

    """
    lettersGuessed: list, what letters have been guessed so far

    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    """

    unguessed = ''
    for i in string.ascii_lowercase:
        if i not in lettersGuessed:
            unguessed += i
    return unguessed


def hangman(secretWord):

    """
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.
    """

    print ('Welcome to the game, Hangman!')
    print ('I am thinking of a word that is ' + str(len(secretWord))
            + ' letters long.')
    print ('-----------')

    guessesleft = 8
    lettersGuessed = []

    while True:

        print ('You have ' + str(guessesleft) + ' guesses left.')
        print ('Available letters: ' + getAvailableLetters(lettersGuessed))

        guess = (input('Please guess a letter:')).lower()

        if guess in secretWord and guess not in lettersGuessed:
            lettersGuessed.append(guess)
            print ('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))

        elif guess not in secretWord and guess not in lettersGuessed:
            lettersGuessed.append(guess)
            print ('Oops! That letter is not in my word: '
                   + getGuessedWord(secretWord, lettersGuessed))
            guessesleft -= 1

        elif guess in lettersGuessed:
            print ("Oops! You've already guessed that letter: "
                   + getGuessedWord(secretWord, lettersGuessed))

        print ('-----------')

        if isWordGuessed(secretWord, lettersGuessed):
            print ('Congratulations, you won!')
            break

        elif guessesleft == 0:
            print ('Sorry, you ran out of guesses. The word was '
                   + secretWord + '.')
            break


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
