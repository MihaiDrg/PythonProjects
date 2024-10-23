import random

# print(f"{rock_anim} \n Computer chose: \n {paper_anim} \n YOU LOSE!!!")

rock_anim = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper_anim = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors_anim = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

your_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 fos Scissors.\n"))
computer_input = random.randint(0, 2)

if your_input == 0:
    if computer_input == 0:
        print(f"{rock_anim} \n Computer chose: \n {rock_anim} \n DRAW!")
    elif computer_input == 1:
        print(f"{rock_anim} \n Computer chose: \n {paper_anim} \n YOU LOSE!!!")
    else:
        print(f"{rock_anim} \n Computer chose: \n {scissors_anim} \n YOU WIN!!!")
elif your_input == 1:
    if computer_input == 0:
        print(f"{paper_anim} \n Computer chose: \n {rock_anim} \n YOU WIN!!!")
    elif computer_input == 1:
        print(f"{paper_anim} \n Computer chose: \n {paper_anim} \n DRAW!")
    else:
        print(f"{paper_anim} \n Computer chose: \n {scissors_anim} \n YOU LOSE!!!")
elif your_input == 2:
    if computer_input == 0:
        print(f"{scissors_anim} \n Computer chose: \n {rock_anim} \n YOU LOSE!!!")
    elif computer_input == 1:
        print(f"{scissors_anim} \n Computer chose: \n {paper_anim} \n YOU WIN!!!")
    else:
        print(f"{scissors_anim} \n Computer chose: \n {scissors_anim} \n DRAW!")
else:
    print("You dindt chose a good number, YOU LOSE!!!")
