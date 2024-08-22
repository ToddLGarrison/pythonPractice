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
# for char in range(1, pw_letters + 1):
#     random_char = random.choice(letters)
#     pw_easy += random_char
# for num in range(1, pw_num + 1):
#     random_num = random.choice(numbers)
#     pw_easy += random_num
# for sym in range(1, pw_sym +1):
#     random_sym = random.choice(symbols)
#     pw_easy += random_sym
for char in range(1, pw_letters + 1):
    pw_easy += random.choice(letters)
for num in range(1, pw_num + 1):
    pw_easy += random.choice(numbers)
for sym in range(1, pw_sym +1):
    pw_easy += random.choice(symbols)

print(f"Easy password {pw_easy}")


#hard
pw_holder = []
pw_hard = ""

for char in range(0, pw_letters):
    pw_holder += random.choice(letters)
for num in range(0, pw_num):
    pw_holder += random.choice(numbers)
for sym in range(0, pw_sym):
    pw_holder += random.choice(symbols)

print(pw_holder)
random.shuffle(pw_holder)
print(pw_holder)
for char in pw_holder:
    pw_hard += char
print(f"Hard password {pw_hard}")