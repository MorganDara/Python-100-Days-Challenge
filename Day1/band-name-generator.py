# First program of the 100 days coding challenge
'''
    Author: DARA Morgan
    Date: 11/08/2021
    Version: 1.0.0
    Description: Simple program that generate
     a band name for you using given information
'''

def generate_band_name(params):
    return ' '.join(params)

def handle_loop(user_response):
    if(user_response[0] == 'y'):
        return True
    else:
        return False

def main():
    print("\nWelcome to the band name generator\n")
    print("Answer the following question and we will generate a cool band name for you.\n")
    pet_name = input("What's your city's name? ")
    city_name = input("What's your pet's name? ")
    params = [city_name, pet_name]
    band_name = generate_band_name(params)
    print("\nYour band name could be: " + band_name + "\n")

if __name__=='__main__':
    loop = True
    while(loop):
        main()
        loop = handle_loop(input("Continue? (Y/N) "))