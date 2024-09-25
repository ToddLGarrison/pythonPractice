def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

continue_calculation = True

while continue_calculation == True:
    first_num = int(input("What's the first number?: "))
    operation = input(f"+\n-\n*\n/\nPick an operation: ")
    second_num = int(input("What's the next number?: "))

