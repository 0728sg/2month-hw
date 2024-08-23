import random
from colorama import Fore, Style, init
from art import tprint
init(autoreset=True)
def choose_word():
    words = ['choza', 'batirhanchik', 'mercedes', 'BMW', 'porsche']
    return random.choice(words)
def display_hangman(tries):
    stages = [
        """
            ------
            |    |
            |    O
            |   /|\\
            |   / \\
            |
         -----
         """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / 
           |
        -----
        """,
        """
          ------
          |    |
          |    0
          |   /|\\
          |
          |
        -----
        """
        """
           ------
           |    |
           |    O
           |   /|
           |    
           |
        -----
        """,
        """
          ------
          |    |
          |    O
          |    |
          |    
          |
        -----
        """,
        """
              ------
              |    |
              |    O
              |    
              |    
              |
           -----
           """,

        """
           ------
           |    |
           |    
           |    
           |    
           |
        -----
        """,
    ]
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA, Fore.WHITE]
    color_stage = stages [tries]
    colored_stage = f"{colors[6 - tries]}{color_stage}{Style.RESET_ALL}"
    return colored_stage
def play_game():
    word = choose_word()
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    tprint("давайте играть в виселицу", font="random")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Введите букву или слово целиком: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(Fore.BLUE + f"Вы уже угадывали букву {guess}.")
            elif guess not in word:
                print(Fore.RED + f"Буквы {guess} нет в слове.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(Fore.GREEN + f"Отлично! Буква {guess} есть в слове!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(Fore.BLUE + f"Вы уже угадывали слово {guess}.")
            elif guess != word:
                print(Fore.RED + f"Слово {guess} не верно.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Некорректный ввод.")

        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    if guessed:
        print(Fore.GREEN + f"Поздравляем! Вы угадали слово {word}!")
    else:
        print(Fore.RED + f"Вы не угадали слово. Загаданное слово было "
                         f"{word}. Возможно, повезет в следующий раз!")
if __name__ == "__main__":
    play_game()
