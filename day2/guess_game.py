import random

def choose_word():
    words = ["python","Coding","code","data",
             "programming","visual"]
    return random.choice(words)

def word_status(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += " _ "
    return display


def word_guessing_game():
    secret_word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Word Guessing Game")
    print("******************")
    print("Secret Word:", word_status(secret_word,guessed_letters))

    while attempts > 0 :
        guess = input("Guess A Letter:").lower()

        if (len(guess) != 1) or (not guess.isalpha()):
            print("You must enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            attempts -= 1
            print(f"No letter '{guess}' occurs in the word.")
            print(f"You have {attempts} attempts remaining.")
        else:
            occur = secret_word.count(guess)
            print(f"Letter '{guess}' occurs {occur} times")

        current_status = word_status(secret_word, guessed_letters)
        print("Secret Word:", current_status)

        if " _ " not in current_status:
            print("Congretulations! You GUESS the word.")
            break
    if " _ " in current_status:
        print(f"You ran out of attempts! The word was: {secret_word}")

word_guessing_game()