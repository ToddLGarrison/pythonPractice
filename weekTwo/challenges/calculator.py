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

# print(operations["*"](5,5))
def calculator():
    continue_calculation = True
    first_num = float(input("What's the first number?: "))

    while continue_calculation == True:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        second_num = float(input("What's the next number?: "))

        sum = operations[operation_symbol](first_num, second_num)

        should_continue = input(f"Do you want to continue calculating with {sum}? (y/n): ").lower()

        if should_continue == "y":
            first_num = sum
        else:
            continue_calculation = False
            print("\n" * 20)
            calculator()

calculator()