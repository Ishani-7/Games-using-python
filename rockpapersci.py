import random
while(True):
    print("Rock ")
    print("Paper ")
    print("Scissors ")
    choice1=input("Player one choice: ")
    option=["Rock","Paper","Scissors"]
    choice2=random.choice(option)
    print("Player two choosed:",choice2)
    if (choice1=="Rock" and choice2=="Paper") or (choice1=="Paper" and choice2=="Scissors") or (choice1=="Scissors" and choice2=="Rock"):
        print("Player two wins")
        break
    if (choice2=="Rock" and choice1=="Paper") or (choice2=="Paper" and choice1=="Scissors") or (choice2=="Scissors" and choice1=="Rock"):
         print("Player one wins")
         break
    if choice1==choice2:
        print("Try again")
        print("------------------")
    else:
        print("Invalid choice, please choose from the option below")


