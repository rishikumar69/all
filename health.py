import datetime

def getime():
    return datetime.datetime.now()

foex = (int(input("What you want to add \n press 1 to add food \n press 2 to add Exersise \n :")))

def health(foex):
    if foex == 1:
        print("Who are you \n Press 1 for Rishi \n Press 2 for harry \n Press 3 for Om")
        a = (int(input(':')))
        if a == 1:
            food = input("What You Have ate :")
            f = open("rishi.txt", "a")
            f.write(food)
            f.close()
            print("Suseccfully Noted.")

        if a == 2:
            food = input("What You Have ate :")
            f = open("harry.txt", "a")
            f.write(food)
            f.close()
            print("Suseccfully Noted.")

        if a == 3:
            food = input("What You Have ate :")
            f = open("rohan.txt", "a")
            f.write(food)
            f.close()
            print("Suseccfully Noted.")

        elif a > 3 :
            print("Wrong Input!!!")

    elif foex == 2:
        print("Who are you \n Press 1 for Rishi \n Press 2 for harry \n Press 3 for Om")
        a = (int(input(':')))

        if input == 1:
            print("Who are you \n Press 1 for Rishi \n Press 2 for harry \n Press 3 for Om")
            a = (int(input(':')))
            if a == 1:
                food = input("What You Have done:")
                f = open("rishiforex.txt", "a")
                f.write(food)
                f.close()
                print("Suseccfully Noted.")

            if a == 2:
                food = input("What You Have done:")
                f = open("harryforex.txt", "a")
                f.write(food)
                f.close()
                print("Suseccfully Noted.")

            if a == 3:
                food = input("What You Have done :")
                f = open("rohanforex.txt", "a")
                f.write(food)
                f.close()
                print("Suseccfully Noted.")

            elif a > 3:
                print("Wrong Input!!!")

        elif foex > 2:
            print("Wrong input!!!")

health(foex)







