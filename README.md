# HangmanProject
A game that makes a player guess a word by guessing it, one letter at a time.
When the player guesses a letter wrongly he loses one life.
The game ends when the player runs out of lives or when the player succesfully guesses the word.
I used python libraries such as random to introduce randomness into the game, as well used the powerful selection methods of numpy arrays to find and replace letters.

## Milestone 1
I cloned a github repository `Hangman_Test` to obtain a template code.
Used the in-built python function `input` to ask the user of the game for an input

## Milestone 2
Created the attributes of the class using the __init__ function which includes `number of letters` and `word`
Modified the `ask_letter` method to prompt the user for a single character in case the user enters more than 1 character
Also, added code to check if a particular letter has already been tried and prompt the user

## Milestone 3
Updated the `check_letter` to check if a letter entered is part of the word in question. 
If the letter is in the word, the user is prompted of the success and that letter is revealed in the word on screen
If the letter is not in the word, the user is prompted of the failure and his number of lives is reduced by one
Completed the ask lettter method by including code that would check if the letter entered by the user is valid.

## Milestone 4
I completed the program by adding code that will recursively ask the user for an input until the user guesses the word or the numbe rof lives is finished

## Bonus
Added code to visualize a part of the hangman whenever a wrong answer is provided
