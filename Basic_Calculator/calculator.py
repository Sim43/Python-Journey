import clear

import art


def calculate(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    else:
        return num1 / num2


def recursive_func():
    first_number = float(input("What's the first number: "))
    again = True
    result = 0
    yorn = ""
    while again:
        operation = input("+\n-\n*\n/\nPick and operation: ")
        second_number = float(input("What's the second number: "))
        result = calculate(first_number, operation, second_number)
        print(f"{first_number} {operation} {second_number} = {result}")
        yorn = input(
            f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation, or type 'e' to exit: ")
        if yorn == "n":
            clear.clear()
        if yorn == "y":
            first_number = result
        elif yorn == "n":
            again = False
            recursive_func()
        else:
            return


print(art.logo)
recursive_func()
print("Goodbye!")