import random

a = int(input("Enter The Value of a: "))
b = int(input("Enter The Value of b: "))

ran = random.randint(a, b)
ran2 = random.randint(a, b)


i = 0
user1 = 1
user2 = 1

print("Player 1st turns...")
while True:
    i = i + 1
    a = int(input("Enter The number: "))

    if a == ran:
        print(f"you have left chances {10-i}")
        print(f"WOW You Choice the correct Number in {i} chances...")
        user1 = user1 + 1
        break

    elif a > ran:
        print(f"you have left chances {10-i}")
        print("Try a smaller number...")

    elif a < ran:
        print(f"you have left chances {10-i}")
        print("Try a bigger number...")

    else:
        print("Something went wrong...")

    if i == 10:
        print(f"player 1 have scored {user1} points")
        break

i = 0
user2 = 0
print("Player 2nd turns...")
while True:
    i = i + 1
    a = int(input("Enter The number: "))

    if a == ran2:
        print(f"you have left chances {10-i}")
        print(f"WOW You Choice the correct Number in {i} chances...")
        user2 = user2 + 1
        break

    elif a > ran2:
        print(f"you have left chances {10-i}")
        print("Try a smaller number...")

    elif a < ran2:
        print(f"you have left chances {10-i}")
        print("Try a bigger number...")

    else:
        print("Something went wrong...")

    if i == 10:
        print(f"player 2 have scored {user2} points")
        break

if user1 < user2:
    print("Player 1 wins ...")

elif user1 > user2:
    print("Player 2 wins ...")

else:
    print("the match is draw...")