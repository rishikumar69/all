import random

print("Welcome To STONE PAPER SCIZER !!!!!!")

computer = ['Stone', 'paper', 'sizer']
# all variable
computer_score = 0
your_score = 0
i = 1

while True:
    i = i + 1
    if i == 10:
        break
    user_input = int(input("Choice One\n1---Stone\n2---Paper\n3---Scizzer\n:"))
    ran = random.choice(computer)

    if ran == 'Stone' and user_input == 1:
        print("The Match Is Draw")

    elif ran == 'paper' and user_input == 2:
        print("The Match Is Draw")

    elif ran == 'sizer' and user_input == 3:
        print("The Match Is Draw")

    elif ran == "Stone" and user_input == 2:
        print("You Win!!!!")
        your_score = your_score + 1

    elif ran == "paper" and user_input == 3:
        print("You Win!!!")
        your_score = your_score + 1

    elif ran == "sizer" and user_input == 1:
        print("You Win!!!")
        your_score = your_score + 1

    elif ran == "Stone" and user_input == 3:
        print("You Lose!!!")
        computer_score = computer_score+1

    elif ran == "paper" and user_input == 1:
        print("You Lose!!!")
        computer_score = computer_score + 1

    elif ran == "sizer" and user_input == 2:
        print("You Lose!!!")
        computer_score = computer_score + 1



    else:
        print("Error")
print("Your Score is",your_score)
print("Computer Score is",computer_score)

if your_score > computer_score:
    print("You won the game!!!!")

elif your_score == computer_score:
    print("This Game Is Drawn")

else:
    print("Computer won the game ")
