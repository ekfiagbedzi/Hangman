# HangmanProject
A game that makes a player guess a word by guessing it, one letter at a time.
When the player guesses a letter wrongly he loses one life.
The game ends when the player runs out of lives or when the player succesfully guesses the word.
I used python libraries such as random to introduce randomness into the game, as well used the powerful selection methods of numpy arrays to find and replace letters.
![code-snapshot](https://user-images.githubusercontent.com/71975468/166810568-f05ae7bc-b226-4d41-aeb2-9492a4430110.png)

## Code and Environment setup
I created a github repository `Hangman_Test` 
I created a conda environment with libraries = versions:
python = 3.8
numpy = 1.21.5

## Class creation and attribute setup
Created class called `Hangman` and setup attributes as shown in screenshot below
![code-snapshot](https://user-images.githubusercontent.com/71975468/166812847-487d7ae9-4e48-4b59-a461-25f29b44f8b6.png)

## Method definitions of the class
Created the `ask_letter` method to prompt the user
Used the in-built python function `input` to ask the user 
of the game for an input

for a single character in case the user enters more than 1 character
Also, added code to check if a particular letter has already been tried and prompt the user
Created the `check_letter` to check if a letter entered is part of the word in question. 
If the letter is in the word, the user is prompted of the success and that letter is revealed in the word on screen
If the letter is not in the word, the user is prompted of the failure and his number of lives is reduced by one
Completed the ask lettter method by including code that would check if the letter entered by the user is valid.
![code-snapshot](https://user-images.githubusercontent.com/71975468/166813663-3e387bce-6151-4c2e-af1b-9e6f09087489.png)


## Function to play game
I created a function `play_game` that will start the game

![code-snapshot](https://user-images.githubusercontent.com/71975468/166813986-4b87045c-5e51-48f6-969a-5311bfa48e8a.png)

## Hangman Visualization
Added code to visualize a part of the hangman whenever a wrong answer is provided. First the arms, then head, neck torso and legs
<img width="1440" alt="image" src="https://user-images.githubusercontent.com/71975468/166814426-ff586532-2ca5-48da-8d19-1d7f02b92724.png">
