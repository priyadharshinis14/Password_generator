import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ""
    
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: Select at least one character type!"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# User Input
try:
    length = int(input("Enter password length: "))
    letters = input("Include letters? (y/n): ").lower() == 'y'
    numbers = input("Include numbers? (y/n): ").lower() == 'y'
    symbols = input("Include symbols? (y/n): ").lower() == 'y'

    if length <= 0:
        print("Length must be positive!")
    else:
        password = generate_password(length, letters, numbers, symbols)
        print("\nGenerated Password:", password)

except ValueError:
    print("Invalid input! Please enter correct values.")
