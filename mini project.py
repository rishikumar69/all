class Library:

    def __init__(self,ls_of_book,name_lib):
        self.name = name_lib
        self.book_list = ls_of_book
        self.user_dict = {}
        self.name_lib = name_lib
    def add_book(self,book_name):
        self.book_list.append(book_name)

    def lend_book(self,book_name,user):
        if book_name not in self.user_dict:
            self.user_dict.update({book_name:user})
            print("THE Book will be delivered to your home...")

        else:
            print(f"The Book is not avaiable the book is taken by {user}")

    def return_book(self,book_name):
        if book_name is self.user_dict:
            self.book_list.append(book_name)

        else:
            print("the book is already in the list...")

    def display_book(self):
        for item in self.book_list:
            print(item)

    while True:
        print(f"Welcome to library")
        print("1 to display books")
        print("2 to leand a book")
        print("3 to return a book")
        print("4 to add a book")
        inpu = int(input(":"))

        if inpu == 1:
            display_book()

        elif inpu == 2:
            lend_bo = input("Enter The book of name: ")
            user_name= input("Enter your name: ")
            lend_book(lend_bo,user_name)

        elif inpu == 3:
            re_book = input("Enter the name of book: ")
            return_book(re_book)

        elif inpu == 4:
            ne = input("Enter the name of the book: ")
            add_book(ne)

        else:
            print("Not valid Input!!!")

        print("Type the q to quit and c to continue ")
        qc = input()

        if qc == "c":
            continue
        elif qc == "q":
            quit()

rishi = Library(["rishi","science","maths","python"],"Rishi")
