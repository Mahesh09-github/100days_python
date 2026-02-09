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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
******************************************************************************** 
      ''' ) 
print("Welcome to the Treasure Hunt!")
print("Your Mission is to find the Treasure!!")
print("""You are at a hill, 
                type Climb or Tunnel to move """)

#Enter the move to make at the hill
cross_road = input()
if cross_road == "Tunnel":
    print("Sorry, you fell into a hole. Game Over!!")
elif cross_road == "Climb":
    print("""It is night and You have come to a Forest,
          you can either wait for morning or cross the forest at night,
          type morning  or night to cross the forest""")
    lake = input()
    if lake == "Night":
        print("Sorry, you were attacked by a Bear. Game Over!!")
    elif lake == "Morning":
        print("""You hve crossed the forest and
               you have come to a cave which has 3 door
              type Red,Blue or Yellow to open the door""")
        door = input()
        if door == "Red":
            print("Sorry, you were burned by fire. Game Over!!")
        elif door == "Blue":
            print("Sorry, you were eaten by beasts. Game Over!!")
        elif door == "Yellow":
            print("Congratulations, you found the Treasure!!")