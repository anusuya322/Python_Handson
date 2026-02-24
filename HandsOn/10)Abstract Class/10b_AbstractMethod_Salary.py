from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
    def __init__(self,name,id):
        self.name=name
        self.id=id
class FullTimeEmployee(Employee):
    def __init__(self,name,id,salary,allowances):
        super().__init__(name,id)
        self.salary=salary
        self.allowances=allowances
    def calculate_salary(self):
        return self.salary+self.allowances
class Intern(Employee):
    def __init__(self,name,id,salary,Time):
        super().__init__(name,id)
        self.salary=salary
        self.Time=Time
    def calculate_salary(self):
        return self.salary*self.Time

f=FullTimeEmployee("Seetha",100,50000,5000)
print("Full Time Emp Salary:",f.calculate_salary())
i=Intern("Anu",77,4000,6)
print("Intern Salary:",i.calculate_salary())

