import random

while True:
    dice_amount = input("How many dice are we rolling? ")

    if dice_amount.isdigit():
        dice_amount = int(dice_amount)
        if 1 <= dice_amount <= 20:
            break
    print("must be between 1 and 20")


while True:
    dice_sides = input("How many sides on each die? ")

    if dice_sides.isdigit():
        dice_sides = int(dice_sides)
        if 1 <= dice_sides <= 100:
            break
    print("must be between 1 and 100")



while True:
    result = "|"
    for die in range(1, dice_amount + 1):
        result += f"{random.randint(1, dice_sides)}|"
    print(result)
    
    user_input = input("Press Enter to continue or 'q' to quit: ")
    if user_input == "q":
        break