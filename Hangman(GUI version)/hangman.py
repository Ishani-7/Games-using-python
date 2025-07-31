import json
import random
import tkinter as tk
from tkinter import messagebox
import os


def get_word_from_difficulty(level):
    if level.upper() not in ("EASY", "MEDIUM", "HARD"):
        raise ValueError("Invalid Level Choice")
    json_path = os.path.join(os.path.dirname(__file__), "hangman.json")
    with open(json_path) as file_obj:
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
        pass  # Keep logic clean


def display_word(user_list):
    return " ".join(user_list)


# --------------------- GUI Setup --------------------- #
root = tk.Tk()
root.title("Hangman Game")
root.geometry("500x400")

# Ask for difficulty using a dropdown
difficulty_var = tk.StringVar(value="EASY")
difficulty_menu = tk.OptionMenu(root, difficulty_var, "EASY", "MEDIUM", "HARD")
difficulty_menu.pack(pady=10)


# Start Button
def start_game():
    global computer_word, hint, user_word, USER_ATTEMPT

    try:
        level = difficulty_var.get()
        computer_word, hint = get_word_from_difficulty(level)
    except ValueError as e:
        messagebox.showerror("Error", str(e))
        return

    USER_ATTEMPT = 6
    user_word = ["_"] * len(computer_word)
    label_hint.config(text=f"Hint: {hint}")
    label_word.config(text=display_word(user_word))
    label_attempts.config(text=f"Remaining Attempt: {USER_ATTEMPT}")
    entry_letter.config(state="normal")
    btn_guess.config(state="normal")


def guess_letter():
    global USER_ATTEMPT

    letter = entry_letter.get().upper()
    entry_letter.delete(0, tk.END)

    if not letter.isalpha() or len(letter) != 1:
        messagebox.showwarning("Invalid Input", "Please enter a single letter.")
        return

    previous_display = "".join(user_word)
    update_user_word_based_on_choice(letter)
    new_display = "".join(user_word)

    if previous_display == new_display:
        USER_ATTEMPT -= 1

    label_word.config(text=display_word(user_word))
    label_attempts.config(text=f"Remaining Attempt: {USER_ATTEMPT}")

    if "".join(user_word) == computer_word:
        messagebox.showinfo("Hangman", "🎉 You Win!")
        root.quit()

    elif USER_ATTEMPT == 0:
        messagebox.showinfo("Hangman", f"💀 You Lose! The word was {computer_word}")
        root.quit()


# Labels
label_hint = tk.Label(root, text="Hint: ", font=("Arial", 14))
label_hint.pack(pady=5)

label_word = tk.Label(root, text="", font=("Courier", 28))
label_word.pack(pady=5)

label_attempts = tk.Label(root, text="Remaining Attempt: 6", font=("Arial", 12))
label_attempts.pack(pady=5)

entry_letter = tk.Entry(
    root, font=("Arial", 16), width=5, justify="center", state="disabled"
)
entry_letter.pack(pady=5)

btn_guess = tk.Button(
    root, text="Guess", font=("Arial", 12), command=guess_letter, state="disabled"
)
btn_guess.pack(pady=5)

btn_start = tk.Button(root, text="Start Game", font=("Arial", 12), command=start_game)
btn_start.pack(pady=10)

root.mainloop()
