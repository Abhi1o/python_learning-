#guess head & tail
import random
print("\nlet's play guess game!\n") 
guess = input("Choice Heads or Tails? type 'Heads' or 'Tails' ").lower()

if guess=="heads" or guess=="tails":

    if guess == "heads":
        guess=1
    elif guess == "tails":
        guess=0
    
#computer is guessing
    random = random.randint(0,1)
    if random == 1:
        print("\ncomputer choses Heads\n")

    else:
        print("\ncomputer choses Tails\n")
    print

#checking computer and your guess
    if random == guess:
        print("\t-->YOU WIN<--\n")

    else:
        print("\t-->YOU LOSE<--\n")

else:
    print("you have enter wrong spelling\n")
    print("\t -->YOU LOSE<--\n")





