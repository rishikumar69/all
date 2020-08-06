from data import data


class Student:
    no_of_students = 0
    students_lst = []

    def __init__(self, name, dob, roll_no):
        self.name = name
        self.dob = dob
        self.roll_no = roll_no
        Student.no_of_students += 1
        f = open("data.txt", "w+")
        f.writelines(name)

while True:
    print(f"1-- To Add Student\n2-- To see Student List\n"
          f"3-- To See Student Details\n4-- To Delete Student\nq-- To Quit")
    n = int(input(':'))

    if n == int(1):
        student_name = input("Enter Student Name: ")
        student_dob = int(input("Enter the DOB of the Student: "))
        student_roll_no = int(input("Enter The Roll No. of Student: "))
        student_name = Student(student_name, student_dob, student_roll_no)

    if n == int(2):
        f = open("data.txt", "r+").read()
        print(f)

    elif n == int(3):
        pass

    elif n == int(4):
        pass

    elif n == "q":
        break
    else:
        print("Wrong Input!!!")
