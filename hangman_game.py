HANGMAN_ASCII_ART = r"""  _    _
 | |  | |
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |
                     |___/
"""

MAX_TRIES = 6
# A change
print(HANGMAN_ASCII_ART, "\n",MAX_TRIES)

#import random
#print(random.randint(5,10))

secret_word = input("Please enter a word: ")
pattern = "_ " * len(secret_word)
print(pattern)

letter_guessed = input("\nGuess a letter: ")
old_letters_guessed = ['a', 'p', 'c', 'f']
def check_valid_input(letter_guessed, old_letters_guessed):
    letter_guessed = letter_guessed.lower()
    if len(letter_guessed) > 1:
        return False
    elif letter_guessed.isalpha() == False:
        return False
    elif letter_guessed in old_letters_guessed:
        return False
    else:
        return True

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input(letter_guessed, old_letters_guessed) is True:
        old_letters_guessed.append(letter_guessed)
        return True
    elif check_valid_input(letter_guessed, old_letters_guessed) is False:
        print("X")
        old_letters_guessed.sort()
        print(' -> '.join(old_letters_guessed))
        return False

check_valid_input(letter_guessed, old_letters_guessed)
try_update_letter_guessed(letter_guessed, old_letters_guessed)

print(old_letters_guessed)
def show_hidden_word(secret_word, old_letters_guessed):
    for letter in secret_word:
        if letter not in old_letters_guessed:
            secret_word = secret_word.replace(letter, "_")
    print(' '.join(secret_word))

show_hidden_word(secret_word, old_letters_guessed)

def check_win(secret_word, old_letters_guessed):
    guessed_word = 0
    for letter in secret_word:
        if letter in old_letters_guessed:
            guessed_word += 1
        else:
            return False
    return True

print(check_win(secret_word, old_letters_guessed))

HANGMAN_PHOTOS = {1:"""    x-------x\n""", 2:"""
    x-------x
    |
    |
    |
    |
    |
    \n""", 3:"""
    x-------x
    |       |
    |       0
    |
    |
    |
    \n""", 4:"""
    x-------x
    |       |
    |       0
    |       |
    |
    |
    \n""", 5:
r"""
    x-------x
    |       |
    |       0
    |      /|\
    |
    |
    """
"""\n""", 6:
r"""    x-------x
    |       |
    |       0
    |      /|\
    |      /
    |
    """
"""\n""", 7:
r"""    x-------x
    |       |
    |       0
    |      /|\
    |      / \
    |
""" }

