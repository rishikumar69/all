class Class:
    num_of_stu = 50
    s1 = "RISHI"
    s2 = "GOLU"
    def __init__(self,name,marks,rollnum):
        self.name = name
        self.marks = marks
        self.rollnum = rollnum


rishi = Class("rishi",66,21)
golu = Class("Golu",33,22)

print(rishi.name,golu.marks)

