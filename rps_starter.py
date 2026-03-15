from random import randint

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# Pick a random number from 1 to 3
num = randint(1,3)

# Turn that random number into the computer's RPS move
if num == 1:
    computer_move = rock
elif num == 2:
    computer_move = paper
else:
    computer_move = scissors

# Ask a user to enter their move
user_move = input("enter your move: ").lower()
if user_move == "rock":
    user_move = rock
elif user_move == "paper":
    user_move = paper
else:
    user_move = scissors

# Print the rock, paper, or scissors ASCII art that corresponds to the player's move
print(user_move)

# Print the rock, paper, or scissors ASCII art that corresponds to the computer's move
print(computer_move)

# Figure out who wins and print the result!
if (user_move == rock and computer_move == scissors) or (user_move == scissors and computer_move == paper) or (user_move == paper and computer_move == rock):
    print("You win!")
elif user_move == computer_move:
    print("It's a tie!")
else:
    print("You lose!")