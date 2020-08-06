
usrinp = int(input("Enter th lenth of numbers: "))

usrinp2 = str(usrinp)
i = 0
for i in range(1,usrinp+1):
    inp = int(input("Enter the number: "))
    inp2 = str(inp)
    if inp2[::-1] == inp2:
        print("Pelendrome")

    elif inp2[::-1] != inp2:
        for r in range(inp,inp+100):
            r1 = str(r)
            i = i+1
            if r1[::-1] == r1:
                print(f"The next Plendrone of {inp} is {r1[::-1]}")
                break