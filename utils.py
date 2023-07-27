import random
import re
from constants import DIFFICULTY_LEVELS, WORDS_LENGTH

def show_difficulty_menu():
    """MENU DE DIFICULDADE"""
    print("Escolha o Nivel de Dificuldade:")
    difficulty_settings = ""

    while not difficulty_settings:
        
        for k,v in DIFFICULTY_LEVELS.items():
            print(f"{k} - {v.upper()}")

        difficulty_settings = input("Escolha sua dificuldade:")
        
        if difficulty_settings not in DIFFICULTY_LEVELS.keys():
            print(f"{difficulty_settings} nao é uma opção valida")
            difficulty_settings = ""

    return difficulty_settings

def get_random_word(difficulty_settings):
    """SELECIONA UMA PALAVRA ALEATORIA EM RELAÇÃO AO NIVEL DE DIFICULDADE"""
    with open("static\words.txt", mode="r") as f_words:
        words = []
        for word in f_words.readlines():
            w = word.strip()
            min,max = WORDS_LENGTH[difficulty_settings]

            if min <= len(w) <= max:
                words.append(w)

    max_index = len(words)-1
    random_index = random.randint(0,max_index)
    selected_word = words[random_index]

    return selected_word


def get_total_tries(selected_word, difficulty_settings):
    """EXIBE O TOTAL DE TENTATIVAS PARA RESOLVER O PROBLEMA"""
    unique_letters = set(selected_word)
    total_tries = 1.5* len(unique_letters)
    if difficulty_settings == "1":
        total_tries += 2
    elif difficulty_settings == "3":
        total_tries -= 2
        total_tries = min([total_tries, 18])

    total_tries = round(total_tries)
    return(total_tries)

def play_hangman(selected_word,difficulty_settings):
    """FUNCIONAMENTO DO JOGO"""
    total_tries = available_tries = get_total_tries(selected_word, difficulty_settings)
    current_state = ["_" for letter in selected_word]
    guessed_letters = []

    while "_" in current_state and available_tries:
        print(f"\n\n##tentativa numero {total_tries - available_tries + 1} de {total_tries} ##")
        for char in current_state:
            print(char, end=" ")

        guess = ""
        while not guess:
            guess = input("\nTente uma letra:").lower()
            if len(guess) != 1 or not re.match("[a-z]",guess):
                print("Invalido. tente novamente utilizando 1 letra.")
                guess = ""

        if guess not in guessed_letters:
            guessed_letters.append(guess)

            if guess in selected_word:
                positions = [m.start() for m in re.finditer(guess, selected_word)]

                for index in positions:
                    current_state[index] = guess

            else:
                    available_tries -= 1
        else:
            print(f"{guess} já foi usada.")

    return available_tries


