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
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************
''')
print('''
Welcome to Treasure Island.
Your mission is to find the treasure.
''')

first_choise = input("You're at a cross road. Where do you want to go? Type \"Left\" or \"Right\"\n").lower()

if first_choise == "left":
    second_choise = input("Now you come to a lake. There is an island in the middle of the lake. Type \"Wait\" to wait for a boat or type \"Swim\" to swim across.\n").lower()
    if second_choise == "swim":
        third_choise = input("You arrive at the island unharmed. There is a house with 3 doors. One Red, one Yellow and one Blue. Wich colour do you choose?\n").lower()
        if third_choise == "yellow":
            print('''
||====================================================================||
||//$\\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\\||
||(100)==================| FEDERAL RESERVE NOTE |================(100)||
||\\\$//        ~         '------========--------'                \\\$//||
||<< /        /$\              // ____ \\\                         \ >>||
||>>|  12    //L\\\            // ///..) \\\         L38036133B   12 |<<||
||<<|        \\\ //           || <||  >\  ||                        |>>||
||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
||<<|      L38036133B        *\\\  |\_/  //* series                 |>>||
||>>|  12                     *\\\/___\_//*   1989                  |<<||
||<<\      Treasurer     ______/Franklin\________     Secretary 12 />>||
||//$\                 ~|UNITED STATES OF AMERICA|~               /$\\\||
||(100)===================  ONE HUNDRED DOLLARS =================(100)||
||\\\$//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\\$//||
||====================================================================||
            ''')
            print("Congratulations! You win!")
        elif third_choise == "blue":
            print("A stone falls on your head and you die. GAME OVER")
        elif third_choise == "red":
            print("You fall in lava and you die. GAME OVER")
        else:
            print("You didn't make a good choise. GAME OVER")
    elif second_choise == "wait":
        print("Waiting is a waste of time, never do that again. GAME OVER.")
    else:
        print("You didn't make a good choise. GAME OVER")
elif first_choise == "right":
    print("When you're walking, you fall in a deep hole and you died. GAME OVER")
else:
    print("You didn't make a good choise. GAME OVER")
