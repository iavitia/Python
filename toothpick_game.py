user1 = input("enter player 1's name: ") 

user2 = input("enter player 2's name: ") 

  

  

toothpicks = 13 

while True: 

    print(toothpicks * "| ") 

    print(f'There are {toothpicks} left') 

    print("\r") 

    while True: 

        user_1_input = input(f"How many do you take, {user1}? ") 

         

        if user_1_input.isdigit(): 

            user_1_input = int(user_1_input) 

            if 1 <= user_1_input <= 3: 

                toothpicks -= user_1_input 

                break 

        print("You can only take 1, 2, or 3") 

    print("\r") 

     

    if toothpicks <= 0: 

        print(f"{user1} won!") 

        break 

    print(toothpicks * "| ") 

    print(f'There are {toothpicks} left') 

    while True: 

        user_2_input = input(f"How many do you take, {user2}? ") 

         

        if user_2_input.isdigit(): 

            user_2_input = int(user_2_input) 

            if 1 <= user_2_input <= 3: 

                toothpicks -= user_2_input 

                break 

        print("You can only take 1, 2, or 3") 

    print("\r") 

    if toothpicks <= 0: 

        print(f"{user2} won!") 

        break 

 