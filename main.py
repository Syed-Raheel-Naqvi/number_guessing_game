import random  # Import the random module to generate a random number for the user to guess.

# Print a welcome message and game instructions to the user
print("Welcome to the Number Guessing Game!") # Greet the player and introduce the game
print("Guess a number between 50 and 100.!") # Explain the range of number to guess from
print("You have 5 attempts.") # Tell the player the number of attempts they have
print("Let's start!") # Encourage the player to start the game

# Generate a random number between 50 and 100 (inclusive) for the user to guess
number_to_guess = random.randrange(50, 101)  # The upper bound randrange is exclusive, so we use 101 to include 100

chances = 5   # Set the maximum number of attempts the user has to guess the number

guess_counter = 0  # Initialize a counter to keep track of the number of gusses made  

 #Start a loop that continues as long as the user has attempts left
while guess_counter < chances:

   guess_counter += 1  # Increment the guess counter by 1 for each attempt
   user_guess = int(input("Please enter your guess: ")) # Prompt the user to enter their guess and convert it to an integer

   if user_guess == number_to_guess: 
     print(f"The number is {number_to_guess} and you find it right!! in the {guess_counter} attept")
     break #Exit the loop if the user guesses the correct number 

  # Check if the user has run out of attempts and still has not guessed the correct number
   elif guess_counter >= chances and user_guess != number_to_guess:
     print(f"Oops sorry, the number is {number_to_guess} better luck next time!")

   elif user_guess < number_to_guess:
     print("Your guess is very low, try again!")

   elif user_guess > number_to_guess:
     print("Your guess is very high, try again!")
    
