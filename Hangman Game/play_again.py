# when the game is finished, ask for replay


from playgame import playgame

def play_again(word_to_list):
    # Ask the user if he / she wants to play again
    again = input('Do you want to play again?\n'
                  'Type y or n\n')
    if again == 'y':
        playgame(word_to_list)
    else:
        print('GoodBye then!')