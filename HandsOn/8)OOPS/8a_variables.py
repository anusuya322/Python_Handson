class Student:
    scl_name="SSV"
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
obj=Student("Anu",14)
print(obj.scl_name)
print(obj.name)
print(obj.roll_no)
print("After changing school")
Student.scl_name="MP"
print(obj.scl_name)
print(obj.name)
print(obj.roll_no)


