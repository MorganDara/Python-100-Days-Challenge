'''
    Author: DARA Morgan
    Date: 04/10/2021
    Version: 1.0.0
    Description: Simple program to encrypt/decrypt a text
    using caesar code
'''
A_ASCII = 97
Z_ASCII = 122

def encode(message, shift_number):
    message = list(message)
    result = []

    for l in message:
        ascii_val = ord(l)
        if ascii_val >= A_ASCII and ascii_val <= Z_ASCII:
            result += chr((ascii_val + shift_number - A_ASCII) % 26 + A_ASCII)
        else:
            result += l

    return ''.join(result)

def decode(message, shift_number):
    pass

def main():
    mainloop = True
    choice = ""
    while mainloop:
        choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        message = input("Type your message:\n").lower()
        shift_number = int(input("Type the shift number:\n"))

        if choice == "encode":
            result = encode(message, shift_number)
            print(f"Here is the encoded message: {result}")
        elif choice == "decode":
            result = decode(message, shift_number)
            print(f"Here is the decoded message: {result}")

        choice = input("Type 'yes' to coninue or 'no' to stop the program\n").lower()
        if choice == "yes":
            print("\n")
        else:
            mainloop = False

if __name__=="__main__":
    main()