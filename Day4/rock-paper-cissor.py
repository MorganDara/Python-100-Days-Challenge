from random import randint

ROCK_IMAGE = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

PAPER_IMAGE = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

SCISSOR_IMAGE = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
ROCK, PAPER, SCISSOR = "0", "1", "2"

ASCII_IMAGES = {
    ROCK: ROCK_IMAGE,
    PAPER: PAPER_IMAGE,
    SCISSOR: SCISSOR_IMAGE
}

# Win codes
NO_WINNER = 0
PLAYER = 1
COMPUTER = -1



def decide_winner(player_one, player_two):
    if(player_one == player_two):
        return NO_WINNER
    else:
        if (player_one == ROCK and player_two == SCISSOR) or (player_one == PAPER and player_two == ROCK) or (player_one == SCISSOR and player_two == PAPER):
            return PLAYER
        else:
            return COMPUTER

def game():
    available_choices = [ROCK, PAPER, SCISSOR]
    user_input = input(f"What do you choose? Type {ROCK} for Rock, {PAPER} for Paper and {SCISSOR} for Scissors.\n")

    while user_input not in available_choices:
        user_input = input("Only type 0, 1 or 2\n")
    
    computer_choice = str(randint(0,2))

    print(f"\nYou chose: {ASCII_IMAGES[user_input]}\n\nComputer chose: {ASCII_IMAGES[computer_choice]}\n")

    winner = decide_winner(user_input, computer_choice)
    if winner == NO_WINNER:
        print("Draw\n")
    else:
        if winner == PLAYER:
            print("You win!\n")
        else:
            print("You lose\n")

if __name__=='__main__':
    game()