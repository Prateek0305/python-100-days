import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
      __________)
      (____)
---.__(___)
'''

user_input = int(input("Enter 1 for rock, 2 for paper, 3 for scissors: "))

if user_input == 1:
    print("You chose rock")
    print(rock)
elif user_input == 2:
    print("You chose paper")
    print(paper)
elif user_input == 3:
    print("You chose scissors")
    print(scissor)
else:
    print("Invalid input")

computer_choice = random.randint(1, 3)

if computer_choice == 1:
    print("Computer chose rock")
    print(rock)
    if user_input == 1:
        print("It's a draw")
    elif user_input == 2:
        print("You win")
    elif user_input == 3:
        print("You lose")
elif computer_choice == 2:
    print("Computer chose paper")
    print(paper)
    if user_input == 1:
        print("You lose")
    elif user_input == 2:
        print("It's a draw")
    elif user_input == 3:
        print("You win")
elif computer_choice == 3:
    print("Computer chose scissors")
    print(scissor)
    if user_input == 1:
        print("You win")
    elif user_input == 2:
        print("You lose")
    elif user_input == 3:
        print("It's a draw")

