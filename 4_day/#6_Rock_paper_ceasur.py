#rock  paper scissor
import random

rock = '''
rock

    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
paper

    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = ''' 
scissors

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

person=int(input("enter your choice?enter 0 for rock,1 for paper and 2 for seeissore: "))





if person<0 or person>2:
    print("you have enter wrong choice. ")
else:
    print(game_images[person])
    computer=random.randint(0,2)
    print("computer choice ")
    print(game_images[computer])

    if person==0 and computer==2:
        print("you win")
    elif person==2 and computer==0:
        print("you lose")
    elif person==computer:
        print("Game draw")
    elif computer>person:
        print("you lose")
    elif person>computer:
        print("you win")

# print