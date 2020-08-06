harrsapple = int(input("ENTER THE NUMBER OF APPLE HARRY HAS: "))
mn = int(input("Enter the minimum range : "))
mx = int(input("Enter the maximum range : "))

if mn != mx:
    for i in range(mn,mx+1):
        if i%2 == 0:
            print(f"{i} is the diviser of {harrsapple}")

        else:
            print(f"{i} is not the diviser of {harrsapple}")

elif mx == mn:
    for i in range(mn,mx+1):
        if i%2 == 0:
            print(f"{i} is the diviser of {harrsapple}")

        else:
            print(f"{i} is not the diviser of {harrsapple}")

