#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Easy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
for i in range(0, nr_numbers):
    l = random.randint(0, len(numbers) - 1)
    m = numbers[l]
    n = str(m)
    password += n
for i in range(0, nr_letters):
    a = random.randint(0, len(letters) - 1)
    b = letters[a]
    password += b
for i in range(0, nr_symbols):
    z = random.randint(0, len(symbols) - 1)
    y = symbols[z]
    password += y

print(password)

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

random_password = ""
for i in range(0, len(password)):
    d = random.randint(0, len(password) - 1)
    random_password += password[d]

print("The password is: ", random_password)