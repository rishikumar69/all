# FOR PRACTICING AND THE TASK IS GIVEN BY CODEWITHHARRY
num = int(input("Enter How Many Number You Want To Enter: "))
lst = []


#taking input from the user
for i in range(1,num+1):
    inp2 = int(input("Enter the number: "))
    inp = str(inp2)
    if inp > '10':
        if inp[::-1] == inp:
            print("Palendrome")

        elif inp[::-1] != inp:
            for r2 in range(inp2, inp2 + 100):
                r = str(r2)
                if r[::-1] == r:
                    print(f"The Palendrome Of {inp} Is The {r}")
                    break
