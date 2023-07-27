from utils import get_random_word, show_difficulty_menu,play_hangman



if __name__ == "__main__":
    difficulty_settings = show_difficulty_menu()
    selected_word = get_random_word(difficulty_settings)
    player_wins = play_hangman(selected_word,difficulty_settings)
    
    if player_wins:
        print("PARABENS! VOCE GANHOU O JOGO")
    else:
        print("INFELIZMENTE VOCÊ PERDEU")

    print(f"A PALAVRA É {selected_word}")
