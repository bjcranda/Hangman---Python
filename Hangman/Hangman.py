from string import ascii_lowercase
from words import get_random_word


def get_num_attempts():
    while True:
        num_attempts = input("How many attempts to guess do you want? (Up to 25 attempts)")
        try:
            num_attempts = int(num_attempts)
            if 1 <= num_attempts <= 25:
                return num_attempts
            else:
                print("{0} is not between 1 and 25".format(num_attempts))
        except ValueError:
            print("{0} is not a whole number between 1 and 25".format(num_attempts))


def get_min_word_length():
    while True:
        min_word_length = input("What do you want the minimum word length to be? (between 4 and 16 letters)")
        try:
            min_word_length = int(min_word_length)
            if 4 <= min_word_length <= 16:
                return min_word_length
            else:
                print("{0} is not between 4 and 16".format(min_word_length))
        except ValueError:
            print("{0} is not a whole number between 4 and 16".format(min_word_length))


def get_display_word(word, idxs):
    if len(word) != len(idxs):
        raise ValueError("Word length and indices length are not the same")
    displayed_word = ''.join([letter if idxs[i] else '*' for i, letter in enumerate(word)])
    return displayed_word.strip()


def get_next_letter(remaining_letters):
    if len(remaining_letters) == 0:
        raise ValueError("There are no remaining letters")
    while True:
        next_letter = input("Choose another letter: ").lower()
        if len(next_letter) != 1:
            print("{0} is not a single letter".format(next_letter))
        elif next_letter not in ascii_lowercase:
            print("{0} is not a letter".format(next_letter))
        elif next_letter not in remaining_letters:
            print("{0} has been guessed before.".format(next_letter))
        else:
            remaining_letters.remove(next_letter)
            return next_letter


def play_hangman():
    print("Starting a new game of Hangman...")
    attempts_remaining = get_num_attempts()
    min_word_length = get_min_word_length()
    print("Selecting a word...")
    word = get_random_word(min_word_length)
    print()

    idxs = [letter not in ascii_lowercase for letter in word]
    remaining_letters = set(ascii_lowercase)
    wrong_letters = []
    word_solved = False
    while attempts_remaining > 0 and not word_solved:
        print("Word: {0}".format(get_display_word(word, idxs)))
        print("attempts Remaining: {0}".format(attempts_remaining))
        print("Previous Guesses: {0}".format(' '.join(wrong_letters)))

        next_letter = get_next_letter(remaining_letters)

        if next_letter in word:
            print("{0} is in the word!".format(next_letter))

            for i in range(len(word)):
                if word[i] == next_letter:
                    idxs[i] = True
        else:
            print("{0} is Not in the word!".format(next_letter))

            attempts_remaining -= 1
            wrong_letters.append(next_letter)
        if False not in idxs:
            word_solved = True
        print()

    print("The word is {0}!".format(word))

    if word_solved:
        print("Congratulations! You are the best!")
    else:
        print("Better luck next time!")

    try_again = input("Would you like to play again? [Y] ")
    return try_again.lower() == "y"


if __name__ == "__main__":
    while play_hangman():
        print()

