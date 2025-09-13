from pathlib import Path

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
/______/______/______/______/______/______/______/______/______/______/______
*******************************************************************************
      ''')
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
direction= input('Type "left" or "right"\n')

if direction== "left":
    print("You've come to a lake. There is an island in the middle of the lake. ")
else:
    print("Fall into a hole.\n Game Over.")
    quit()

choice= input(' Type "wait" to wait for a boat. Type "swim" to swim across.\n')
if choice== "wait":
    print("You arrive at the island unharmed. There is a house with 3 doors.")
else:
    print("Attacked by trout.\n Game Over.")
    quit()

door=input("One red, one yellow and one blue. Which colour do you choose?\n ")

if door=="red":
    print("Burned by fire.\n Game Over.")
elif door=="blue":
    print("Eaten by beasts.\n Game Over.")
elif door=="yellow":
    print("You Win!")
else:
    print("Game Over.")
