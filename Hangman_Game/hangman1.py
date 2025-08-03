import json
import random


def get_word_from_difficulty(level):
    if level.upper() not in ("EASY", "MEDIUM", "HARD"):
        raise ValueError("Invalid Level Choice")
    with open("hangman.json") as file_obj:
        data = json.load(file_obj)
    user_level_data = data[level]
    computer_data = random.choice(user_level_data)
    computer_word, computer_hint = computer_data
    return computer_word.upper(), computer_hint


def update_user_word_based_on_choice(letter):
    global user_word
    global computer_word

    if letter in computer_word:
        for index in range(len(computer_word)):
            if computer_word[index] == letter:
                user_word[index] = letter
    else:
        "Invalid choice"


def display_word(user_list):
    print("".join(user_list))


difficulty_level = input("Enter the difficulty level: (EASY/MEDIUM/HARD): ")
computer_word, hint = get_word_from_difficulty(difficulty_level)
length_of_computer_word = len(computer_word)
user_word = ["_"] * length_of_computer_word
USER_ATTEMPT = 6

while USER_ATTEMPT > 0:
    print(f"Remaining Attempt: {USER_ATTEMPT}")
    print(f"Hint: {hint}")
    user_letter = input("Enter a letter: ").upper()
    update_user_word_based_on_choice(user_letter)
    if "".join(user_word) == computer_word:
        print("You Win")
        break
    display_word(user_word)
    USER_ATTEMPT = USER_ATTEMPT - 1
else:
    print("You Loose")
    print(f"The word was {computer_word}")