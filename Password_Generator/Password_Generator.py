# Password Generator

# Import random + define character pools
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

# Step 1: Collect user inputs for the password composition
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []

# Step 2: Build the password list using random choices
for letter in range(0, nr_letters):
    password.append(random.choice(letters))

for symbol in range(0, nr_symbols):
    password.append(random.choice(symbols))

for number in range(0, nr_numbers):
    password.append(random.choice(numbers))

# Step 3: Shuffle and convert list into final password string
random.shuffle(password)

real_password = ""
for words in password:
    real_password += words

print(f"Your password is: {real_password}")