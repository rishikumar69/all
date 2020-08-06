a = (int(input("Press 1 to Create Account\nPress 2 to Login\nPress 3 to exit\n: ")))

if a == 1:
    can = (str(input("Enter Your Name: ")))
    cap = input("Enter Your Password: ")
    f = open("createac.txt")
    f.newlines(can)
    f.close()
    f = open("creatrpass.txt")
    f.writelines(cap)
    f.close()

elif a == 2:
    askname = input("Enter Your Name: ")
    f = open("createac.txt")
    f.readlines()
    if askname == f:
        askpass = input("Enter Your Password: ")
        f = open("creatrpass.txt")
        f.readlines()
        if askpass == f:
            print("Login...")

        elif askpass != f:
            print("Wrong Password!!!")

    elif askname != f :
        print("Wrong Input!!!")

elif a == 3:
    exit()

else:
    print("Wrong Input")



