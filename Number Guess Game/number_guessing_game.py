
# 11.Number Guessing Game
# In this exercise we will build a simple game that lets the user guess a
# random number.

# 1.Create a function start() that will start the game
# 2.Create a function called play_again() which will ask the users if
# they want to play again when the game ends.

#Print “I am thinking of a number from 1-10. Can you find it?
# You have 5 tries.”

# Check if the input of the user is an int.
# Create an infinite loop that allows the users to guess as many times
# as they need…

#Print “Guess what it is: “.
# Read in the user’s guess as an int.
# If the user guessed correctly, print Congratulations! You guessed it.
# Ask the user if he/she wants to play again..

# If the user’s guess is lower than the random number, print “Nope.
# It’s lower than that. Try again.” to the console.
# If the user’s guess is higher than the random number, print “Nope.
# It’s higher than that. Try again.” to the console.
# Track how many guesses the user has made and print “Congratulations!
# You guessed it in # tries.” to the console if the user guesses correctly,
# where # is the number of guesses.


def start():
    import random
    number = random.randint(1, 10)

    def play_again():
        again = input('Do you want to play again? \n Type y or n \n')
        if again =='y':
            start()
        else:
            print('No problem! Bye!')


    print("I am thinking of a number from 1-10."
                          " Can you find it?"
                          " You have 5 tries.\n")
    # flag to exit the loop
    flag = True
    # counter to count the tries
    counter = 0
    while flag:
        guess = int(input('Give a number from 1-10 \n'))
        counter += 1
        if guess < number:
            print('Nope! \n It’s higher than that. Try again.')
        if guess > number:
            print('Nope! \n It’s lower than that. Try again.')
        elif guess == number:
            print(f"You guessed it in {counter} tries.")
            flag = False

    play_again()


start()
