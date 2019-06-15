# ADVANCED EXERCISES - PYTHON DAY 2


# 1.Even Numbers
# Write a program which can filter even numbers in a list by using filter
# function. The list is: [1,2,3,4,5,6,7,8,9,10].

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
even_numbers_filter = list(filter(lambda num: num % 2 == 0, numbers))

# print(even_numbers)
# print(even_numbers_filter)


# 2.Square Elements
#Write a program that accepts a list and returns the square of each element.
# The list is: [1,2,3,4,5,6,7,8,9,10].


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square_numbers = [num ** 2 for num in numbers]
square_numbers_map = list(map(lambda num: num ** 2, numbers))

# print(square_numbers)
# print(square_numbers_map)



# 3.Squared Even Numbers
#Write a program which uses map() and filter() to make a list of elements
# that are the squares of the even numbers in [1,2,3,4,5,6,7,8,9,10].

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

square_even_numbers = list(filter(lambda x: x % 2 == 0, map(lambda y: y ** 2, numbers)))
# or the other way around
square_even_numbers2 = list(map(lambda y: y ** 2, filter(lambda x: x % 2 == 0, numbers)))

# print(square_even_numbers)
# print(square_even_numbers2)



# 4.Find Certain Numbers
# Write a function find_numbers(min, max) that will find all numbers that
# are a multiple of 7 but not a multiple of 5.
# First, try getting it right with an explicit for loop. If you have it up
# and running, write a second version that avoids explicit for loops and
# uses filter and lambda only!


def find_numbers(min , max):
    # store the range of the given numbers
    numbers = list(range(min, max + 1))

    # double filter the array
    output_list = list(filter(lambda x: x % 7 == 0, filter(lambda x: x % 5 == 0, numbers)))

    return output_list


# print(find_numbers(5, 700))



# 5.Online Shop
# Assume you have an online shop, and you have a list of orders.
# You don’t like that people order in small quantities, which is why you
# would like to add an additional CHF 10 to the total price, for all orders
# that are below CHF 100 in total.

# Write a short Python function compute_totals that returns a list of
# 2-tuples. Each tuple consists of the order number and the total price.
# The total price should be increased by CHF 10 if the total is less than
# CHF 100.
# TODO with filter()
def compute_totals(input_list):
    list_of_lists = []
    output_list = []

    # extract the id and multiple the value with quantity
    for _dict in input_list:
        list_of_lists.append([_dict['id'], _dict['quantity'] * _dict['price_per_item']])

    # check if the total price is under 100 CHF
    for _list in list_of_lists:
        if _list[1] < 100:
            _list[1] += 10

        output_list.append(tuple(_list))

    return output_list


orders = [

    {
        'id': 'order_001',
        'item': 'Introduction to Python',
        'quantity': 1,
        'price_per_item': 32,
    },
    {
        'id': 'order_002',
        'item': 'Advanced Python',
        'quantity': 3,
        'price_per_item': 40,
    },
    {
        'id': 'order_003',
        'item': 'Python web frameworks',
        'quantity': 2,
        'price_per_item': 51,
    },
]

# totals = compute_totals(orders)
# print(totals)
# totals is [('order_001', 42), ('order_002', 120), ('order_003', 102)]



# 6.Input and Range
# Given an integer n, write a program that generates a dictionary with
# entries from 1 to n. For each key i, the corresponding value should
# be i*i.


def range_dict(_max):
    my_dict = {}
    for i in range(1, _max + 1):
        my_dict[i] = i ** 2

    return my_dict

# or with dictionary Comprehension
def range_dict2(_max):
    return  {i: i ** 2 for i in range(1, _max + 1)}


# print(range_dict(10))
# print(range_dict2(10))

# for n=10:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}



# 7.List Comprehension
# Using List comprehension generate a list where the values are the
# squares of 1 to 20 (both included). Then print the last 5 elements
# in the list.

original_list = list(range(1,21))
sqrs_list = [num ** 2 for num in original_list][-5:]

# print(sqrs_list)


# 8.Print Style
# Write a small script that will print numbers 1-10 in a way that if
# the number is even it prints the number, if the number is odd it print
# underscore _:

# _2_4_6_8_10
list_1_10 = list(range(1, 11))

output_string = ''
for num in list_1_10:
    if num % 2 != 0:
        output_string += '_'
    else:
        output_string += str(num)

# print(output_string)



# 9.BMI Calculator
# Print “Let’s calculate your BMI (kg/m2)” to the console.
# Ask the user about the weight in KG.
# Ask the user about the height in CM.
# Read the users weight as a float.
# Read the users height.
# Define a function to calculate the BMI and show info if they are
# underweight, overweight or normal weight.

def bmi_calculator():

    print("Let’s calculate your BMI (kg/m2)")
    weight_kg = float(input('What is your weight in kg? \n'))
    height_cm = int(input('What is you height in cm? \n'))

    bmi = round(weight_kg / ((0.01 * height_cm) ** 2), 1)

    print(f'Your BMI is: {bmi}')
    if bmi <= 18.5:
        return 'You must eat more, you are underweight!!'
    elif 18.5 < bmi <= 25:
        return 'Congrats, you are normal'
    elif 25 < bmi:
        return 'Stop eating!! You are overweight'


# print(bmi_calculator())



# 10.Shopping List
# What am I buying?
# Create a shopping list app, in which the user can add and remove items
# from his shopping list using the console.
# 1. Create a function called help_menu() which is going to show the users a
#   help menu for your simple app.
# Example: Press ‘a’ to add items to the shopping list. Press ‘s’ to show
# the items in the list, ‘r’ to remove and ‘q’ to quit the app
# 2. Create a function show_items() which reads the list and shows the items to
#   the user. Each item should have an id number.
# 3. Create a function add_item() which allows the user to add a new item to
#   the list. Ask the user for the position of the item when adding, if None add the item to the end of the list.
# 3. Create a function remove_item() to remove an item form the list also by
#   asking for the position.


def shopping_list():
    # a list to store the items
    items_list = []

    def help_menu():
        print("Press \n"
              "h: help menu \n"
              "s: show items \n"
              "a: add item \n"
              "r: remove item  \n"
              "q: quit \n")

    def add_item():
        new_item = input('What do you want to add?\n')
        item_index = input('In which position\n')
        if item_index == None or not item_index.isdigit():
            items_list.append(new_item)
        else:
            items_list.insert(int(item_index), new_item)

    def show_items():
        if len(items_list) == 0:
            print('There are no items on the list, nothing to show!')
        else:
            for i in range(len(items_list)):
                print(f"{i + 1}: {items_list[i]}")

    def remove_item():
        if len(items_list) != 0:
            item_index = input('From which position\n')
            items_list.pop(int(item_index) - 1)
        else:
            print('The list is empty, nothing to remove!')

    # initialise the program with the help menu
    help_menu()

    flag = True
    while flag:
        user_input = input('Type your choice \n')
        if user_input == 'q':
            print('Thank you Bye!!')
            flag = False
        elif user_input == 'h':
            help_menu()
        elif user_input == 'a':
            add_item()
        elif user_input == 'r':
            remove_item()
        elif user_input == 's':
            show_items()


# shopping_list()


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


# start()



# Bonus
# 1.Hangman
# In this exercise we are going to build the old hangman game.
# For this one we are using this file as a data source: Data source
# First try to read the file using open() function from python.
# Create a function to get the user’s input, take into account that the
# user is only allowed to type one letter at a time. No numbers or words.

# If the user types the same letter over again, let the user know he used
# that letter already.

# The user is allowed to make 7 incorrect guesses.
# Print the information every time the user guesses a letter.


def hangman():
    import random

    # convert the words to a list
    f = open('words_list.txt', 'r')
    list_f = f.readlines()

    # pick a random word
    word = list_f[random.randint(0, len(list_f))]

    # convert the word to a list of letters
    word_to_list = list((word)[0:-1]) # remove the empty space at the end

    # just for testing purposes print the word
    print(f"The word is: {word}")

    # instructions of the game
    print("\tInstructions:\n"
          "To quit the game simply type 'quit'.\n"
          "You only have 7 tries for this game.\n\n"
          "This is the word we are looking for:")
    print('_' * len(word_to_list) + '\n')

    # variable to track the tries
    tries = 7

    # mask the word with '_'
    remaining_word = ['_' for i in word_to_list]
    print("Type the next letter or 'quit' to exit the game\n")


    # end loop when user tries 7 seven times of type 'quit' or complete the puzzle
    while tries > 0:

        # print the remaing of the word
        print(f"Remaining word: {''.join(remaining_word)}")

        # the user type the letter or 'quit'
        answer = input(f"You have {tries} tries remaining\n")

        # if quit -> break
        if answer == 'quit':
            print('Bye!!')
            break
        # elif the input letter is in the array of letter
        elif answer in word_to_list:
            print('You found a correct letter')
            for index in range(len(word_to_list)):
                # and substitute the underscores with the letter
                if word_to_list[index] == answer:
                    remaining_word[index] = answer

        # print that he made a mistake
        else:
            print('You answered wrong')
        # decrease the user remaining tries
        tries -= 1

        # if the user find the word break the loop
        if ''.join(remaining_word).find('_') == -1:
            print("You have completed the word\n"
                  "CONGRATS!!")
            break

    again = input('Do you eant to play again?'
                  'Type y or n\n')
    if again == 'y':
        hangman()
    else:
        print('GoodBye then!')



hangman()

