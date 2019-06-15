# pick a word fro the .txt


def pick_random_word():
    import random

    # read the words from the txt file
    f = open('words_list.txt', 'r')

    # convert the words to a list
    list_f = f.readlines()

    # close the file
    f.close()

    # pick a random word
    word = list_f[random.randint(0, len(list_f))]

    # convert the word to a list of letters
    word_to_list = list(word[0:-1])  # remove the empty space at the end

    return word, word_to_list

