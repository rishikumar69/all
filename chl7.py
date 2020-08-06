allname = ["rishi", "a", "b", "c", "d", "e", "f", "g", "h", "i"]

input1 = input("Enter the name: ")

def search():
    if input1 in allname:
        print(f"The Text({input1}) is in the book!!! ")

    else :
        print("Text is not in the book")

    while True:
        input1 = yield

