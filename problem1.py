total = []
sum = 0
print("q to quite")
while True:
    a = input("Enter --- ")
    if a != "q":
        sum = sum + int(a)
        print(f"amount till now:{sum}")
        total.append(a)
    else:
        break

print(f"Total Amount{sum}")
print(total,end= "  ")