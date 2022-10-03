#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

slect_letters = []
slect_symbols = []
slect_numbers = []
for i in range(0, nr_letters):
    slect_letters += random.choice(letters)
for i in range(0, nr_symbols):
    slect_symbols += random.choice(symbols)
for i in range(0, nr_numbers):
    slect_numbers += random.choice(numbers)

all_things = slect_letters + slect_numbers + slect_symbols
your_password = ''.join(random.sample(all_things, len(all_things)))
print(f"Your Password Is: {your_password}")
