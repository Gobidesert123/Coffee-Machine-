from Coffee_M_Menu import MENU

# Setting initial constants. 
water = 500
milk = 400
coffee = 300
money = 0
coffee_continue = True


def purchase(water, milk, coffee, money):
    # Checking if ingredients are sufficient.
    if water >= 0 and milk >= 0 and coffee >= 0:
        water, milk, coffee = deduction(water, milk, coffee)
        quarters, dimes, nickles, pennies, change = coins()
        # After making the purchase this checks again if it is valid.
        if water < 0 or milk < 0 or coffee < 0 or change < 0:
            not_enough(water, milk, coffee, change)
        else:
            print(f"Here is ${change} in change.")
            print(f"Here is your {user_prompt}☕️. Enjoy!")
            money += MENU[user_prompt]['cost']

    return water, milk, coffee, money

# This takes care of all the coins and returns to store all remaining values.
def coins():
    print("Please insert coins")
    quarters = int(input("How many quarters"))
    dimes = int(input("How many dimes"))
    nickles = int(input("How many nickles"))
    pennies = int(input("How many pennies"))

    total_in_quarters = quarters*0.25
    total_in_dimes = dimes*0.1
    total_in_nickles = nickles*0.05
    total_in_pennies = pennies*0.01
    dollars = total_in_pennies + total_in_nickles + total_in_dimes + total_in_quarters
    change = dollars - MENU[user_prompt]['cost']
    return quarters, dimes, nickles, pennies, change

# If there is not enough of something this will run.
def not_enough(water, milk, coffee, change):
    if water < 0:
        print(f'Sorry there is not enough water.')
    if milk < 0:
        print(f'Sorry there is not enough milk.')
    if coffee < 0:
        print(f'Sorry there is not enough coffee.')
    if change < 0:
        print("Sorry that's not enough money.")

# From the originally set constants, we are subtracting the amount of ingredient.
# and returning it to be stored.
def deduction(water, milk, coffee):
    water -= MENU[user_prompt]['ingredients']['water']
    milk -= MENU[user_prompt]['ingredients']['milk']
    coffee -= MENU[user_prompt]['ingredients']['coffee']
    return water, milk, coffee

# This will run while it is true, which is predefined with my constants.
while coffee_continue:
    # Each of the drinks hold different values of ingredients
    user_prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # This will print how much of everything remains.
    if user_prompt == "report":
        print(f'Water: {water}ml')
        print(f'Milk: {milk}ml')
        print(f'Coffee: {coffee}g')
        print(f'Money spent: ${money}') # This is the total money you have spent

    elif user_prompt == "espresso":
        water, milk, coffee, money = purchase(water, milk, coffee, money)

    elif user_prompt == "latte":
        water, milk, coffee, money = purchase(water, milk, coffee, money)

    elif user_prompt == "cappuccino":
        water, milk, coffee, money = purchase(water, milk, coffee, money)

    elif user_prompt == "off":
        # This is supposed to end the code
        print("Powering off Machine...")
        break
    else:
        user_prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()





