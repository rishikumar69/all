num_cal = int(input("Enter how many numbers you want to enter: "))
lst = []
original_lst = lst
for i in range(1,num_cal+1):
    cal = int(input(f"Enter {i} number: "))
    lst.append(cal)

#first method
# print(lst)
lst.reverse()
print(lst)

#second method
lst[::-1]
print(lst)


#Third method

def swaplist(lst):
    lst[0],lst[-1] = lst[-1],lst[0]

    return lst
print(swaplist(lst))

print(f"origianl list is {original_lst} and reverserd list is {swaplist(lst)}")

