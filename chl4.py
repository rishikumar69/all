n = (input("Enter the number: "))


i = 1
while True:
    i = i+1
    if i == n:
        break

    else:

        ans = i + (i-1 | i-2)
        print(ans)
