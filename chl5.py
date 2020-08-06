class Student:
    student_name = []
    student_age = {}
    student_marks = {}

    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks

    def add_student(self,name,age,marks):
        Student.student_name.append(name)
        Student.student_age.append(age)
        Student.student_marks.append(marks)
    def Search_student(self):
        for item in Student.student_name:
            if self == item:
                print(self.name, self.marks, self.marks, self.age)
                break
            else :
                print("No Data!!!")

    def all_student_name(self):
        print(Student.student_name)


    def all_student_marks(self):
        print(f"Marks of {self.student_name} is {self.marks}")
        for item in Student.student_marks:
            if item != self.marks:
                print("No data!!!")

        else :
            pass

rishi = Student("rishi",14,99)
kumar = Student("kumar",13,33)
rishi.all_student_name()

