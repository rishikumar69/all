student_list = []

def ask_name():
    while True:
        con = input("Enter 1 to countinue \nEnter 2 to see list \n enter 3 to exit\n:")
        if con == 1:
            ask = input("Enter the name: ")
            if ask == student_list:
                print("Student is in the list...")

            else:
                print("Student is not in the list...")
                student_list.append(ask)



        elif con == 2:
            print(student_list)

        elif con == 3:
            break

        else:
            print("Wrong Input!!!")
ask_name()
