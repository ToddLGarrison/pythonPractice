# def my_function():
#     for i in range(1, 21):
#         if i == 20:
#             print("You got it!")

try:
    age = int(input("How old is your cat?"))
except ValueError:
    print("You have typed in an invalid number, please try again with a numeric value.")
    age = int(input("How old is your cat?"))

if age > 18:
    print("Thats an old kitty")