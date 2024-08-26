number_to_guess = 69 # Fixed number to guess.
guessed_correctly = False # To track if the player guessed correctly.

print("Welcome to 'Guess the number!'")
print("I'm thinking of a number between 50 and 80. Can you guess what it is?")

while not guessed_correctly : # Loop until the player guessed correctly.
    guess = int(input("Enter your guess: "))

    if guess == number_to_guess:
        print("Congratulations! You guessed correctly!")
        guessed_correctly = True # ends the loop
    else:
        print("Sorry, that's incorrect. Try again!")

play_again = input("Do you want to play again? (yes/no): ").lower()

if play_again == "yes":
    guessed_correctly = False
    while not guessed_correctly:
        guess = int(input("Enter your guess: "))

    if guess == number_to_guess:
        print("Congratulations! You guessed correctly!")
        guessed_correctly = True # ends the loop
    else:
        print("Sorry, that's incorrect. Try again!") 

print("Thanks for playing! ")