import data

menu = data.MENU
resources = data.resources


def report():
    global machine_money
    units = ["ml", "ml", "g"]
    i = 0
    for resource in resources:
        print(f"{resource.title()}: {resources[resource]}{units[i]}")
        i += 1
    print(f"Money: ${machine_money}")


def inset_coins():
    global user_money
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    user_money = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01


def check_money(choice):
    global user_money
    global machine_money
    if user_money >= choice["cost"]:
        machine_money += choice["cost"]
        user_money -= choice["cost"]
        return True
    else:
        user_money = 0
        return False


def sub_resources(choice):
    global resources
    if resources["water"] - choice["ingredients"]["water"] >= 0 and resources["milk"] - choice["ingredients"][
     "milk"] >= 0 and resources["coffee"] - choice["ingredients"]["coffee"] >= 0:
        inset_coins()
        if check_money(choice):
            resources["water"] -= choice["ingredients"]["water"]
            resources["milk"] -= choice["ingredients"]["milk"]
            resources["coffee"] -= choice["ingredients"]["coffee"]
            print(f"Here is ${user_money} in change.\nHere is your {user_choice} ☕. Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded.")
    else:
        for resource in resources:
            if choice["ingredients"][resource] > resources[resource]:
                print(f"Sorry there is not enough {resource}.")


machine_money = 0
user_money = 0
user_choice = ""
while user_choice != "off":
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "report":
        report()
    else:
        if user_choice != "off":
            user_choice_strut = menu[user_choice]
            sub_resources(user_choice_strut)

print("Switched off!")
