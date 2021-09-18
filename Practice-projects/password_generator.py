import random

# list of symbols
# symbols in ascii: [33 -> 47], [58 -> 64], [91 -> 96] and [123 -> 126]
symbols = [chr(i) for i in range(33, 48)] + [chr(i) for i in range(58, 65)]
symbols += [chr(i) for i in range(91, 97)] + [chr(i) for i in range(123, 127)]

# letters in ascii: [65 -> 91]
letters = [chr(i) for i in range(65, 91)] + [chr(i).lower() for i in range(65, 91)]



def gen_password(n_letters, n_symbols, n_numbers):
    password = []
    for i in range(n_letters):
        password.append(random.choice(letters))
    
    for i in  range(n_symbols):
        password.append(random.choice(symbols))
    
    for i in range(n_numbers):
        password.append(str(random.randint(0, 9)))
    
    random.shuffle(password)

    return ''.join(password)

def main():
    print("Welcome to the PyPassword Generator!")
    repeat = True
    error = False
    while repeat:
        try:
            n_letters = int(input("How many letters would you like in your password?\n"))
            n_symbols = int(input("How many symbols would you like in your password?\n"))
            n_numbers = int(input("How many numbers would you like in your password?\n"))
            error = False
            repeat = False
        except:
            error = True

        if error:
            print("\nPlease enter valid numbers\n")
        
    password = gen_password(n_letters, n_symbols, n_numbers)
    print(f"\nHere is your password: {password}")

if __name__=='__main__':
    main()