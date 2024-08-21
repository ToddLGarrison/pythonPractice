import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the password generator")
pw_letters = int(input("How many letters do you want in your password? \n"))
pw_num = int(input("How many numbers do you want in your password? \n"))
pw_sym = int(input("How many symbols do you want in your password? \n"))

# easy
pw_easy = ""
for num in range(0, pw_letters):
    rand_num = random.randint(0, len(letters) - 1)
    pw_easy += (letters[rand_num])
for num in range(0, pw_num):
    rand_num = random.randint(0, len(numbers) - 1)
    pw_easy += (numbers[rand_num])
for num in range(0, pw_sym):
    rand_num = random.randint(0, len(symbols) - 1)
    pw_easy += (symbols[rand_num])

print(pw_easy)


#hard