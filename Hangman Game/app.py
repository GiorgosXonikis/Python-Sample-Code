# Hangman Game
# main script

from instructions import instructions
from pick_random_word import pick_random_word
from playgame import playgame
from play_again import play_again

if __name__ == "__main__":
    # print the instructions
    instructions()

    # pick a random word and convert the word to a list of letters
    word, word_to_list = pick_random_word()

    # just for testing purposes print the word
    print(f"Just for testing purpose -> the word is: {word}")

    # play the game
    playgame(word_to_list)

    # ask for replay
    play_again(word_to_list)

