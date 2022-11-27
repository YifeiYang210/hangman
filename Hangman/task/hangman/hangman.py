import random


def guess_letter_core(set_of_user, choose_word, set_of_guess, suggest_letter, prompt_word, attempts):
    set_of_user.add(suggest_letter)
    if suggest_letter in set_of_guess:  # right guess
        prompt_word_list = list(prompt_word)
        for index, _ in enumerate(prompt_word_list):
            if suggest_letter == choose_word[index]:
                prompt_word_list[index] = choose_word[index]
        prompt_word = ''.join(prompt_word_list)
        set_of_guess.discard(suggest_letter)
    else:  # wrong guess
        print("That letter doesn't appear in the word.")
        attempts -= 1
    return prompt_word, attempts


def check_word_valid(suggest_letter, set_of_user):
    if len(suggest_letter) != 1:  # LenException
        print("Please, input a single letter.")
        return False
    if not suggest_letter.islower():  # UpperException
        print("Please, enter a lowercase letter from the English alphabet.")
        return False
    if suggest_letter in set_of_user:  # already guess
        print("You've already guessed this letter.")
        return False
    return True


def guess_word_init():
    list_of_words = ["python", "java", "swift", "javascript"]
    choose_word = random.choice(list_of_words)
    prompt_word = "-" * len(choose_word)
    set_of_guess = set(choose_word)
    set_of_user = set()
    attempts = 8
    return choose_word, prompt_word, set_of_guess, set_of_user, attempts


def guess_word(choose_word, prompt_word, set_of_guess, set_of_user, attempts, num_of_won, num_of_lost):
    while attempts > 0:
        print()
        print(prompt_word)
        if prompt_word == choose_word:  # won
            print(f"You guessed the word {choose_word}!")
            print("You survived!")
            num_of_won += 1
            break
        suggest_letter = input("Input a letter: > ")  # guess input
        if not check_word_valid(suggest_letter, set_of_user):
            continue
        prompt_word, attempts = guess_letter_core(set_of_user, choose_word, set_of_guess, suggest_letter, prompt_word, attempts)
    else:
        print()
        print("You lost!")
        num_of_lost += 1
    return num_of_won, num_of_lost


# user menu part
def hangman_user_menu():
    num_of_won, num_of_lost = 0, 0
    print("H A N G M A N")

    while True:
        command = input('Type "play" to play the game, "results" '
                        'to show the scoreboard, and "exit" to quit: > ')

        if command == "exit":
            break

        elif command == "results":
            print(f"You won: {num_of_won} times")
            print(f"You lost: {num_of_lost} times")

        elif command == "play":
            # system part
            choose_word, prompt_word, set_of_guess, set_of_user, attempts = guess_word_init()

            # logic part
            num_of_won, num_of_lost = guess_word(choose_word, prompt_word, set_of_guess, set_of_user, attempts,
                                                 num_of_won, num_of_lost)


if __name__ == '__main__':
    hangman_user_menu()
