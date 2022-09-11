# guessTheNumber
A simple game where you have 5 lives to guess a number randomly generated.

## Gameplay
When the console asks you for a number between 1 and 100 you have to type in a number between 1 and 100. If its the correct one then, congratulations you won, if its not the console tells you if the correct number is bigger or smaller giving you the possibility to try again with other number. If you give it 5 shots and without guessing you loose. WHen the console says "type in 1 to play again", type 1 only if you want to play again. 

## functionality
after initializing the variables the program goes by in an infinite while loop asking for the user to type in a number. 
If the number typed in is equal to the random generated number then the win variable value is True, breaking the while loop. Else just compares the typed in number with the random generated one and tells if its bigger or smaller. The win Variable continues to be False so the while loop keeps looping.
