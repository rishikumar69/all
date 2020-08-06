import random

ran = random.randint(1,8)
rohan_user = int(input("Enter The Number {Rohan's table}: "))

tb = []

def rohantab(num):
    for i in range(1,ran):
        tb.append(num*i)

    for i in range(ran,ran+1):
        tb.append((num*i)+1)

    for i in range(ran+1,10+1):
        tb.append(num*i)

rohantab(rohan_user)
print(tb)
i = 0
for item in tb:
    i += 1
    if item != rohan_user*i:
        print(f"Mistake is in {i}th Number ")
        print("HENCE PROVED ROHAN DAS IS A FRAUD !!!")
    elif item == rohan_user:
        pass



