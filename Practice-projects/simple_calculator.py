'''
    Author: DARA Morgan
    Date: 16/10/2021
    Version: 1.0.0
    Description: Simple calculator program
'''

LOGO = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def main():
    print(LOGO)
    mainloop = True
    result = None
    while mainloop:
        if result == None:
            num1 = input("What's the first number?: ")
        else:
            num1 = str(result)
        operator  = input("+\n-\n*\n/\nPick an operation: ")
        num2 = input("What's the next number?: ")
        result = eval(num1 + operator + num2)
        print(f"{num1} {operator} {num2} = {result}")
        ask = input(f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation (type 's' to quit the program): ")
        if ask == 'n':
            result = None
        elif ask == 's':
            mainloop = False

if __name__=='__main__':
    main()