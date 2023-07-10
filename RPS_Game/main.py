import random as rnd;

rps={1:"Rock", 2:"Paper", 3:"Scissors"}
user_option= input("Enter your option: \n 1. Rock \n 2. Paper \n 3. Scissors \n")
user_option= int(user_option)
computer_option=rnd.randint(1,3)
if not (user_option == 1 or user_option == 2 or user_option == 3 ):
    print("Invalid option")
else:

    if user_option == computer_option:
        print("TIE")
        print("Computer option: ", rps[computer_option])
        print("User option: ", rps[user_option])
    elif user_option == 1 and computer_option == 2 or user_option==2 and computer_option==3 or user_option==3 and computer_option==1:
        print("You lose")
        print("Computer option: ", rps[computer_option])
        print("User option: ", rps[user_option])
    else:
        
        print("You win")
        print("Computer option: ", rps[computer_option])
        print("User option: ", rps[user_option])