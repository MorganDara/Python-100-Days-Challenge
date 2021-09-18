from random import choice
from english_words import words
from os import system

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

TITLE = """
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/           
"""
def print_game_state(message, picture, word):
  system("cls")
  print(f"{word}\n\n{message}\n{picture}\n")

def game():
  print(TITLE)
  system("pause")
  guess_word = choice(words).lower()
  user_word = "_" * len(guess_word)

  index = 0
  print_game_state("", HANGMANPICS[index], user_word)
  while index < (len(HANGMANPICS) - 1) and user_word != guess_word:
    message = ""
    letter = input("Guess a letter: ").lower()
    if letter in guess_word and letter not in user_word:
      temp = list(user_word)
      for i in range(len(guess_word)):
        if guess_word[i] == letter:
          temp[i] = letter
      user_word = "".join(temp)
      message = "Well guessed!"
    else:
      if letter not in user_word:
        index += 1
        message = "Wrong guess!"
      else:
        message = f"You have already guessed: {letter}"
    print_game_state(message, HANGMANPICS[index], user_word)
    

  if user_word == guess_word:
    message = f"""You have found the correct word: "{guess_word}"\n"""
    print_game_state(message, HANGMANPICS[index], user_word)
  else:
    message = f"""You lost the game. The correct word was "{guess_word}"\n"""
    print_game_state(message, HANGMANPICS[index], user_word)

if __name__=="__main__":
  game()