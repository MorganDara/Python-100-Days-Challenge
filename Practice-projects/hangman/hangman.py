from random import choice
from english_words import words

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

def game():
  print(TITLE)
  guess_word = choice(words)
  user_word = "*" * len(guess_word)

  index = 0
  while index < (len(HANGMANPICS) - 1) and user_word != guess_word:
    print(f"\nYour guess: {user_word}\n")
    letter = input("Guess a letter: ")
    if letter in guess_word and letter not in user_word:
      temp = list(user_word)
      for i in range(len(guess_word)):
        if guess_word[i] == letter:
          temp[i] = letter
      user_word = "".join(temp)
    else:
      if letter in user_word:
        print("You have already entered this letter")
      else:
        index += 1
        if index < len(HANGMANPICS):
          print(f"\nWrong guess!\n{HANGMANPICS[index]}")

  if user_word == guess_word:
    print(f"""You have found the correct word: "{guess_word}"\n""")
  else:
    print(f"""You lost the game. The correct word was "{guess_word}"\n""")

if __name__=="__main__":
  game()