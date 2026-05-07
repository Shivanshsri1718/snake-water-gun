'''
1 for snake
-1 for water
0 for gun

'''
import random
computer = random.choice([-1,0,1])

yourchoice = input("Enter your choice 'S' OR 'W' OR 'G' : ")

yourdict = {"S":1, "W":-1, "G":0}
your_number_assigned = yourdict[yourchoice]
compdict = {1 : 'S',-1 : 'W',0:'G'}


print (f"YOU CHOSE {yourchoice} AND THE COMPUTER CHOSE {compdict[computer]}")

if(computer == your_number_assigned):
    print("the game is draw!")

else:
    if(computer == -1 and your_number_assigned == 1):
        print("YOU WIN!")

    elif(computer == -1 and your_number_assigned == 0):
     print("YOU LOSE!")

    elif(computer == 1 and your_number_assigned == 0):
        print("YOU WIN!")

    elif(computer == 1 and your_number_assigned == -1):
     print("YOU LOSE!")

    elif(computer == 0 and your_number_assigned == -1):
        print("YOU WIN!")

    elif(computer == 0 and your_number_assigned == 1):
        print("YOU LOSE!")

    else:
        print("something went wrong!")  