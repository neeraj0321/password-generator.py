import random
import string

def random_password():
    length = int(input("Enter password length: "))
    
    if length == 0:
        length = int(input("Your password length must be greater than zero: "))

    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation
    
    chars = ""
    
    while chars=="":
        inc_letters = input("Do you want to include letters? (yes/no): ")
        inc_numbers = input("Do you want to include numbers? (yes/no): ")
        inc_symbols = input("Do you want to include symbols? (yes/no): ")

        if inc_letters.lower() == "yes":
            chars += letters
        if inc_numbers.lower() == "yes":
            chars += numbers
        if inc_symbols.lower() == "yes":
            chars += symbols
        if chars=="":
            print("Enter yes in any of the options: ")
            
    password = ""
    for i in range(length):
        password += random.choice(chars)

    print("Your generated password is:", password)
while True:
    print("Hello, Welcome to random password generator")

    random_password()
    repeat = input("Do you want to generate another password? (yes/no): ")
    if repeat.lower() != "yes":
        break
