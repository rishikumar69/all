string = "13 fekfo 78d9j7j7f7yf78dthy 9898"
number = []

for item in string.split():
    if item.isdigit():
        number.append(item)


print(number)

