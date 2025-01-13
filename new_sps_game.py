import random
print("Let's start the game")
choices=['stone','paper','scissor']

while True:
    computer_choice=random.choice(choices)
    user_choice = input("Enter your choice: ")
    print("computer choice:",computer_choice)
    if user_choice==computer_choice:
        print("Tie")


    if computer_choice == 'stone' and user_choice == 'paper':
        print("You Win!....")

    elif computer_choice == 'scissor' and user_choice == 'stone':
         print("You Win!....")

    elif computer_choice == 'paper' and user_choice == 'scissor':
         print("You Win!....")

    elif computer_choice == 'paper' and user_choice == 'stone':
        print("You Lose....")

    elif computer_choice == 'stone' and user_choice == 'scissor':
        print("You lose....")

    elif computer_choice == 'scissor' and user_choice == 'paper':
        print("You Lose....")
    else:
        print("error")
    choice = str(input("Do you want to play again:(yes/no): "))
    if (choice == "yes"):
        continue
    else:
        print("Game Over")
        break




