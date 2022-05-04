import random
import numpy as np
print_list = [" _____\n| o o |\n|  >  |\n|__v__|\n",
              " _____\n| o o |\n|  >  |\n|__v__|\n" + "   |\n   |\n",
              " _____\n| o o |\n|  >  |\n|__v__|\n" + "   |\n   |\n" + "-------\n|     |",
              " _____\n| o o |\n|  >  |\n|__v__|\n" + "   |\n   |\n" + "-------\n|  |  |" + "\n   |\n   |\n",
              " _____\n| o o |\n|  >  |\n|__v__|\n" + "   |\n   |\n" + "-------\n" + "|  |  |\n   |\n   |\n" + "-------\n|     |\n|     |"]

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''
    def __init__(self, word_list, num_lives=5):

        self.word = random.choice(word_list)
        self.num_letters = len(self.word)
        self.word_guessed = ["_"] * self.num_letters
        self.num_lives = num_lives
        self.list_letter = []
        self.body_count = 0
        self.print_list = [" _____\n| o o |\n|  >  |\n|__v__|\n",
              " _____\n| o o |\n|  >  |\n|__v__|\n" + "   |\n   |\n",
              " _____\n| o o |\n|  >  |\n|__v__|\n" + "   |\n   |\n" + "-------\n|     |",
              " _____\n| o o |\n|  >  |\n|__v__|\n" + "   |\n   |\n" + "-------\n|  |  |" + "\n   |\n   |\n",
              " _____\n| o o |\n|  >  |\n|__v__|\n" + "   |\n   |\n" + "-------\n" + "|  |  |\n   |\n   |\n" + "-------\n|     |\n|     |"]
        
        print("The mistery word has {} characters".format(self.num_letters))
        print("{}".format(self.word_guessed))
        

    def check_letter(self, letter):
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked

        '''

        # checks if entered letter is correct
        if letter in list(self.word):
            letter_indices = np.where(np.array(list(self.word)) == letter)[0]
            # replace "_" with correct letter
            for ind in letter_indices.tolist():
                self.word_guessed[ind] = letter
            print("Nice {} is in the word!".format(letter))
        # subtracts -1 from `num_lives` if letter is incorrect
        else:
            self.num_lives -= 1

            print("Your guess {} was incorrect. You have {} lives left".format(letter, self.num_lives))
            print(self.print_list[self.body_count])
            self.body_count += 1
        print(self.word_guessed)

    def ask_letter(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
        

        while (self.num_lives > 0) & (list(self.word) != self.word_guessed):
            # prompt user for input
            letter = input("Enter a letter: ").lower()
            
            # check the validity of the letter
            if len(letter) > 1:
                print("Please, enter just one character")
            elif letter in self.list_letter:
                print("{} was already tried".format(letter))
            else:
                self.check_letter(letter)
                self.list_letter += [letter]
                
        if self.num_lives == 0:
            print("You lost! The word was {}".format(self.word))
        else:
            print("Congratulations! You won!")

def play_game(word_list):
    game = Hangman(word_list, num_lives=5)
    game.ask_letter()


if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
# %%
