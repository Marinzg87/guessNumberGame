# Project Guess Number Game

## To Do's
- [x] Prepare the to-do list
- [x] Prepare the flow chart
- [x] Prepare comments or pseudo-code
- [x] Write down the functionalities
- [x] Code
- [x] Test
## Breakdown requirements
- [x] computer randomly chooses one number in the range from 1 to 100
- [x] user can choose the game level: easy and hard
- [x] easy level has 10 guesses & hard level has 5 guesses
- [x] user can make a guess
- [x] each guess is checked
	- [x] the match will end the game, and the user wins
	- [x] too high guess
	- [x] too low guess
	- [x] if there are more guesses, the user can make a guess again
	- [x] if there are no more guesses, end the game, and the user lost
## Pseudo-code & Comments
### Comments
In this project, the user can play the guessing game.
Randomly one number in the range from 1 to 100 will be chosen.
We offer two levels: easy with 10 guesses, and hard with 5 guesses.
After guessing, the result will be shown:
- if matches, then the user wins;
- if the guess is higher;
- if the guess is lower;
- how many guesses are left.
### Pseudo-code
```
Welcome message
The message that the computer has chosen the random number from the range 1-100
Ask the user about the level:
		if high:
			number of guesses = 5
		if low:
			number of guesses = 10
While guesses > 0:
	Ask the user to make a guess
	Check the result
	Give back the answer:
		if match:
			winner, the end game
		if higher:
			guess too high, try again, still have this number of guesses
		if lower:
			guess too low, try again, still have this number of guesses
If number of guesses == 0:
	loser, the end game
```

## Functionalities
- the program should randomly choose one number in the range from 1 to 100;
- the program should have two game levels, soft and hard, with soft there are 10 guesses, with hard there are 5 guesses;
- after each guess, the result should be checked, with match it's the end of the game and the user wins, If the guess is too high the user will get the information that the guess is too high and if there are more guesses, can make a guess again, if the guess is too low, the user will get the information that the guess is too low and if there are more guesses if there are no more guesses the user will get the information, about lost and game, and a random number.