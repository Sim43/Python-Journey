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


print(art.logo)
again = "n"
result = 0
while again != "e":
    if again == "n":
        first_number = float(input("What's the first number: "))
        operation = input("+\n-\n*\n/\nPick and operation: ")
        second_number = float(input("What's the second number: "))
        result = calculate(first_number, operation, second_number)
        print(f"{first_number} {operation} {second_number} = {result}")
        again = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation, or type 'e' to exit: ")
        if again == "n":
            clear.clear()
    else:
        first_number = result
        operation = input("+\n-\n*\n/\nPick and operation: ")
        second_number = float(input("What's the second number: "))
        result = calculate(first_number, operation, second_number)
        print(f"{first_number} {operation} {second_number} = {result}")
        again = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation, or type 'e' to exit: ")
print("Goodbye.")