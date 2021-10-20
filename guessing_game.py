"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random




"""Psuedo-code Hints

When the program starts, we want to:
------------------------------------
1. Display an intro/welcome message to the player.
2. Store a random number as the answer/solution.
3. Continuously prompt the player for a guess.
  a. If the guess greater than the solution, display to the player "It's lower".
  b. If the guess is less than the solution, display to the player "It's higher".

4. Once the guess is correct, stop looping, inform the user they "Got it"
     and show how many attempts it took them to get the correct number.
5. Let the player know the game is ending, or something that indicates the game is over.

( You can add more features/enhancements if you'd like to. )
"""
    # write your code inside this function.
def start_game():    
    
    scores = [10]
    
    while True:
        
        print("*** Welcome to the Number Guessing Game!!! ***")
        high_score = min(scores)
        print(f"CURRENT HIGH SCORE: {high_score}")
        RAND_NUMBER = random.randint(1, 10)
        attempt_count = 1
        
        try:
            guessed_number = input("Guess a number between 1 and 10: ")
            guessed_number = int(guessed_number)
            
            if guessed_number > 10 or guessed_number < 1:
                guessed_number = int(input("Sorry that number is out of range. Guess a number between 1 and 10: "))
            
            while guessed_number != RAND_NUMBER:
                if guessed_number > RAND_NUMBER:
                   guessed_number = int(input(f"Please guess again, number is lower than {guessed_number}: "))
                   attempt_count += 1 
                elif guessed_number < RAND_NUMBER:
                   guessed_number = int(input(f"Please guess again, number is higher than {guessed_number}: "))
                   attempt_count += 1
        except ValueError:
            print("Please enter a valid number")
        
        
        if guessed_number == RAND_NUMBER:
                print(f"Got it!! It took you {attempt_count} tries.\nThank you for playing!! ")
                play_again = input("Would you like to play again? (Yes or No?) ")
                if play_again.lower() == 'yes':
                    scores.append(attempt_count)
                elif play_again.lower() == 'no':
                    print("Thank you for playing. Goodbye!")
                    break
        

        
        

  
# Kick off the program by calling the start_game function.
start_game()
