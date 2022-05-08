import random
from words import words_list


def get_secret_word():
    return random.choice(words_list)


def print_hangman(number_try):
    zero = ("\n"
            "————————\n"
            "|     |\n"
            "|\n"
            "|\n"
            "|\n"
            "|\n"
            "|\n"
            "|———————\n"
            "\n")

    one = ("\n"
           "————————\n"
           "|     |\n"
           "|     O\n"
           "|\n"
           "|\n"
           "|\n"
           "|\n"
           "|———————\n"
           "\n")

    two = ("\n"
           "————————\n"
           "|     |\n"
           "|     O\n"
           "|     |\n"
           "|\n"
           "|\n"
           "|\n"
           "|———————\n"
           "\n")

    three = ("\n"
             "————————\n"
             "|     |\n"
             "|     O\n"
             "|     | /\n"
             "|\n"
             "|\n"
             "|\n"
             "|———————\n"
             "\n")

    four = ("\n"
            "————————\n"
            "|     |\n"
            "|     O\n"
            "|   \ | /\n"
            "|\n"
            "|\n"
            "|\n"
            "|———————\n"
            "\n")

    five = ("\n"
            "————————\n"
            "|     |\n"
            "|     O\n"
            "|   \ | /\n"
            "|     |\n"
            "|\n"
            "|\n"
            "|———————\n"
            "\n")

    six = ("\n"
           "————————\n"
           "|     |\n"
           "|     O\n"
           "|   \ | /\n"
           "|     |\n"
           "|    /\n"
           "|\n"
           "|———————\n"
           "\n")

    seven = ("\n"
             "————————\n"
             "|     |\n"
             "|     O\n"
             "|   \ | /\n"
             "|     |\n"
             "|    / \\ \n"
             "|\n"
             "|———————\n"
             "\n")

    hangman_drawing = [zero, one, two, three, four, five, six, seven]
    print(hangman_drawing[number_try])


def get_current_word(secret, letters):
    len_secret = len(secret)
    return_word = ""
    for i in range(0, len_secret):
        if secret[i] in letters:
            return_word += secret[i]
        else:
            return_word += "_"
    return return_word


if __name__ == "__main__":
    MAX_TRY = 7
    current_try = 0
    letter = ""
    secret_word = get_secret_word()
    find_letters = set()
    current_word = get_current_word(secret_word, find_letters)

    print("~~~~~~~~~~~~~~~")
    print("~~~ HANGMAN ~~~")
    print("~~~~~~~~~~~~~~~")
    print(f"\t{current_word}")
    while current_try < MAX_TRY and secret_word != current_word:
        letter = input("> Enter a letter : ")
        if letter in find_letters:
            print("You already proposed this letter...")
        else:
            find_letters.add(letter)
            current_word = get_current_word(secret_word, find_letters)
            if letter in secret_word:
                print("YEAH! Your pick a good letter!")
                print(current_word)
            else:
                print("Oupsie, WRONG letter!")
                current_try += 1
                print(current_word)
        print_hangman(current_try)
    if secret_word == current_word:
        print("++ WIN! ++")
    else:
        print("-- LOSE! --")
        print(f"The secret word was _{secret_word}_")
