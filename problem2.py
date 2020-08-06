def factor(num):
    if num == 0 or num == 1:
        return 1

    else:
        return num * factor(num-1)

def zero(num):
    pass
while True:

    num = int(input("enter the number -- "))
    print(factor(num))