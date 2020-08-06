import random

def swaping(first,last,num):
    for i in range(0,num+1):
        ran = random.randint(0, num - 1)
        swaped = first[i]+" "+last[ran]
        print(swaped)

name_list = []
first = []
last = []

num = int(input("Enter the number of friend: "))

for i in range(0,num):
    name = input("Enter the name : ")
    name_list.append(name)

for item in name_list:
    splited_name = item.split(" ")
    first.append(splited_name[0])
    last.append(splited_name[1])

swaping(first, last, num)
