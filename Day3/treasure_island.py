treasure_image = '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************
'''

default_messages = {
    "welcome": f"{treasure_image}\n\nWelcome to Treasure island.\n",
    "explanations": "Your mission is to find the treasure.\n\n",
    "lost": "Game over.\n",
    "won": "Congratulation.\n",
    "error": "Please enter a valid choice.\n"
}

game_state = {
    "lost": -1,
    "playing": 0,
    "won": 1
}

choices = {
    "start": {
        "text": 'You are at a cross road. Where do you want to go? Type "left" of "right"\n',
        "Game state": game_state['playing'],
        "available choices": ["left", "right"],
    },

    "right": {
        "text": "You fell into a hole.", 
        "Game state": game_state['lost'],
        "available choices": []
    },

    "left": {
        "text": """You've come to a lake. There is an island in the middle of the lake. Type "wait" or "swim"\n""", 
        "Game state": game_state['playing'],
        "available choices": ["wait", "swim"]
    },

    "swim": {
        "text": "You get attacked by an angry trout.", 
        "Game state": game_state['lost'],
        "available choices": []
    },

    "wait": {
        "text": "You arrive at the island unharmed. There is a house with three doors. One red, one yellow and one blue. Which color do you choose?\n", 
        "Game state": game_state['playing'],
        "available choices": ["red", "yellow", "blue"]
    },

    "red": {
        "text": "It's a room full of fire.", 
        "Game state": game_state['lost'],
        "available choices": []
    },

    "yellow": {
        "text": "You found the treasure.", 
        "Game state": game_state['won'],
        "available choices": []
    },

    "blue": {
        "text": "You enter a room of beast.", 
        "Game state": game_state['lost'],
        "available choices": []
    }
}

def game():
    loop = True
    current_choice = choices["start"]
    user_input = ""

    print(default_messages["welcome"])
    print(default_messages["explanations"])

    while(loop):

        if(current_choice["available choices"] != []):
            user_input = input(current_choice["text"])
            if(user_input not in current_choice["available choices"]):
                print(default_messages["error"])
            else:
                current_choice = choices[user_input]
                continue
        else:
            print(current_choice["text"])

        if(current_choice["Game state"] == game_state["lost"] or current_choice["Game state"] == game_state["won"]):
            message_key  = [key for key in game_state if game_state[key] == current_choice["Game state"]][0]
            print(default_messages[message_key])
            loop = False

def main():
    continue_game = True
    user_input = "N"
    while(continue_game):
        game()
        user_input = input("Would you like to continue playing? (Y/N)\n")
        if(user_input[0].upper() == "N"):
            continue_game = False
            print("\n________________________________________________End_______________________________________________\n")

if __name__ == "__main__":
    main()