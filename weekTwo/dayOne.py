name = input("What is your name? \n")
location = input("What is your location? \n")

# def greet():
#     print(f"Hello {name}")
#     print(f"Hello {name}")
#     print(f"Hello {name}")

# greet()

#multi input functions
def greet_with(x, y):
    print(f"Hello {x}")
    print(f"Do you live in {y}?")

greet_with(y = location,x = name)