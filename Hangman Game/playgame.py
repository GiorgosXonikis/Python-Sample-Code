# the main logic of the game


def playgame(word_to_list):

    # variable to track the tries
    tries = 7

    # mask the word with '_'
    remaining_word = ['_' for i in word_to_list]
    print("Let's Begin!\n"
          "Type the letter\n")

    # end loop when user tries 7 seven times incorrect or type 'quit' or complete the puzzle
    while tries > 0:

        # print the remaining of the word
        print(f"Remaining word: {''.join(remaining_word)}")

        try:
            # the user type the letter or 'quit'
            answer = input(f"You have {tries} tries remaining\n")
        except ValueError:
            print("That's not a string!")
        except EOFError:
            print("Please input something....")


        # if the input letter is in the array of letters
        if answer in word_to_list:
            # print message
            print('You found a correct letter')
            for index in range(len(word_to_list)):
                # and substitute the underscores with the letter
                if word_to_list[index] == answer:
                    remaining_word[index] = answer

        # if he made a mistake print the relevant message
        else:
            print('You answered wrong')
        # and decrease the remaining tries by one
            tries -= 1

        # if the user find the word break the loop
        if ''.join(remaining_word).find('_') == -1:
            print("\n##############################"
                  "\nCONGRATS!!"
                  f"\nYou have completed the word: {''.join(remaining_word)}\n"
                  f"with only {7 - tries} mistakes\n")
            break

        # if user type quit or there are no remaining tries ----> break
        if answer == 'quit' or tries == 0:
            print('\nI am sorry you lost....'
                  '\nBye!!')
            break


