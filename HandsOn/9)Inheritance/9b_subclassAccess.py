class SalaryDetails:
    def __init__(self,salary,bonus):
        self._salary=salary
        self.__bonus=bonus
class SubDetails(SalaryDetails):
    def display(self):
        print("Salary:",self._salary)
       #print("Bonus:",self.__bonus)
        try:
            print("Bonus:",self.__bonus)
        except AttributeError:
            print("Cannot access private attribute directly")

obj=SubDetails(60000,7000)
obj.display()