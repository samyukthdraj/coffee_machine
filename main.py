print("HI ALL USE 'WINDOWS + .' TO GET EMOJI KEYBOARD☕\n")
from machine import MENU, resources
from art import logo
PENNY=0.01
NICKEL=0.05
DIME=0.1
QUARTER=0.25

continue_or_not=True
def coin_function():
    print("ENTER YOUR COINS")
    pennys = int(input("PENNIES: \n"))
    nickels = int(input("NICKELS: \n"))
    dimes = int(input("DIMES: \n"))
    quarters = int(input("QUARTERS: \n"))
    total = (PENNY * pennys + NICKEL * nickels + DIME * dimes + QUARTER * quarters)
    print(f"YOUR TOTAL IS ${total}\n")
    return total


def continue_function():
    global continue_or_not
    to_continue = input("TYPE 'YES' TO ORDER ANOTHER COFFEE OR 'NO' TO EXIT: ").lower()
    if (to_continue == 'no'):
        print("THANK YOU FOR USING OUR COFFEE MACHINE, COME BACK SOON!!")
        continue_or_not = False

# TODO: 1. Print the report, this gives us how much ingredients are in the machine

while continue_or_not==True:
    print(logo)
    choice=input("What would you like to have? espresso\latte\cappuccino or check report: ").lower()
    if choice=='report':
        print("WATER: ", resources['water'], "ml")
        print("MILK: ", resources['milk'], "ml")
        print("COFFEE:", resources['coffee'], "g")
    elif choice=='espresso':
        resources['water']-=50
        resources['coffee']-=18
        total=coin_function()
        if (total>= MENU["espresso"]["cost"]):
            print("YOUR ESPRESSO IS READY\n")
            balance=total-MENU["espresso"]["cost"]
            print(f"BALANCE AMOUNT ${balance} IS RETURNED TO THE USER\n")
            continue_function()
        else:
            print(f"NOT ENOUGH COINS YOUR TOTAL IS ${total}")
    elif choice=='latte':
        resources['water'] -= MENU['latte']['ingredients']['water']
        resources['coffee'] -= MENU['latte']['ingredients']['coffee']
        resources['milk'] -= MENU['latte']['ingredients']['milk']
        total = coin_function()
        if (total >= MENU["latte"]["cost"]):
            print("YOUR LATTE IS READY\n")
            balance = total - MENU["latte"]["cost"]
            print(f"BALANCE AMOUNT ${balance} IS RETURNED TO THE USER\n")
            continue_function()
        else:
            print(f"NOT ENOUGH COINS YOUR TOTAL IS ${total}")
    elif choice=='cappuccino':
        resources['water'] -= MENU['cappuccino']['ingredients']['water']
        resources['coffee'] -= MENU['cappuccino']['ingredients']['coffee']
        resources['milk'] -= MENU['cappuccino']['ingredients']['milk']
        total = coin_function()
        if (total >= MENU["cappuccino"]["cost"]):
            print("YOUR CAPPUCCINO IS READY\n")
            balance = total - MENU["cappuccino"]["cost"]
            print(f"BALANCE AMOUNT ${balance} IS RETURNED TO THE USER\n")
            continue_function()
        else:
            print(f"NOT ENOUGH COINS YOUR TOTAL IS ${total}")
    else:
        print("PLEASE ENTER A VALID INPUT\n")

# TODO: 2. As we enter an input, we should decrease the ingredients from the report
# TODO: 2.1 then we should check if the ingredients are sufficient for the choice,
# TODO: 2.2 then initially the money will be zero,
# TODO: 2.3 we should input some money in nickels pennys quarters and dimes then we should return the money
# TODO: 2.4 if excess money was added or say not enough money when there isnt enough money inputted.
