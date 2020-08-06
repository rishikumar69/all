user_input = int(input("Enter Your Age or Year of birth: "))

if user_input <= 100:
    old = (2020 - user_input)+ 100
    print(f"You will we 100 years old in {old} years ")

elif user_input >= 1900:
    givenyear = user_input
    old = user_input + 100
    print(f"you will 100 years old on {old}")

else:
    print("wrong input!!!")

i = 0
while True:
    i = i+1
    print("do you want to know your age at certain year's\n Y for Yes - N for No")
    old = input(":")
    if old =="Y":
        year = int(input("Enter a Year : "))
        user_input = int(input("Enter Your year of birth: "))
        if user_input > 2020:
            print("Something is wrong!!!")

        else:
            future = year - user_input
            print(f"you will be {future} years old in year {year}")
    elif old == "N":
        exit()
        break
    else:
        print("Why you are giving Wrong input ;-)")

    if i == 10:
        break