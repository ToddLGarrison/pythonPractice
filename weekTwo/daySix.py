# # def my_function():
# #     for i in range(1, 21):
# #         if i == 20:
# #             print("You got it!")

# try:
#     age = int(input("How old is your cat?"))
# except ValueError:
#     print("You have typed in an invalid number, please try again with a numeric value.")
#     age = int(input("How old is your cat?"))

# if age > 18:
#     print("Thats an old kitty")


# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        if number % 3 == 0:
            print("Fizz")
        if number % 5 == 0:
            print("Buzz")
        else:
            print(number)

fizz_buzz(20)