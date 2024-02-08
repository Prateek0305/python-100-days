print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
# Welcome message
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

# Input: user chooses left or right direction
input1 = input("You are at a crossroad. Where do you want to go? Type 'left' or 'right'\n").lower()

# Check user's choice and proceed accordingly
if input1 != "left":
    # If user didn't choose left, they fall into a hole
    print("Fall into a hole. Game over")
else:
    # If user chose left, ask them to swim or wait
    input2 = input("Do you want to swim or wait? ").lower()
    # Check user's choice and proceed accordingly
    if input2 != "wait":
        # If user didn't choose to wait, they are attacked by trout
        print("Attacked by trout. Game over")
    else:
        # If user chose to wait, ask them to choose a door
        input3 = input("Choose the door: red, blue, or yellow? ").lower()
        # Check user's choice and proceed accordingly
        if input3 == "red":
            # If user chose red door, they are burned by fire
            print("Burned by fire. Game over")
        elif input3 == "blue":
            # If user chose blue door, they are eaten by beasts
            print("Eaten by beasts. Game over.")
        elif input3 == "yellow":
            # If user chose yellow door, they win
            print("You win!")
        else:
            # If user chose an invalid option, end the game
            print("Game over")
