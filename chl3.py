import inspect

class Student:
    def __init__(self,name,fav_game):
        self.name = name
        self.fav_game = fav_game

    age = 14
    school = "oxford"
    def to_print(self):
        return f"This Student is {self.name},and he is very good boy.he loves to watch {self.fav_game}"


rishi = Student("rishi","WWE")

print(rishi.to_print())
print(inspect.getmembers(rishi))