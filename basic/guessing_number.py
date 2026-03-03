#Guessing Number Game

#Generate a random number between 1 and 100
#Loop
    #Ask: Enter your guess (or type 0 to quit)
    #Guess a number between 1 and 100
    #If guess is 0 -> Exit the game
    #If guess < the number 
        # -> Print "Your guess is too low. Try again!"
    #If guess > the number 
        # -> Print "Your guess is too high. Try again!"
    #if not a number 
        # -> Print "Invalid input. Please enter a valid number."
    #Else (guess = the number) 
        # -> Print "Congratulations! You've guessed the correct number!"
# exit the loo
import random

def guessing_number():
    number_to_guess = random.randint(1, 100)
    print("Welcome to the Guessing Number Game!")
    while True:
        try:
            user_guess = int(input("Guess a number between 1 and 100 (or type 0 to quit):"))
            if user_guess == 0:
                print("Thank you for playing! Goodbye!")
                break
            elif user_guess < 1 or user_guess > 100:
                print("Please guess a number within the range of 1 to 100.")
                continue
            elif user_guess < number_to_guess:
                print("Your guess is too low. Try again!")
            elif user_guess > number_to_guess:
                print("Your guess is too high. Try again!")
            else:
                print("Congratulations! You've guessed the correct number!")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    guessing_number()