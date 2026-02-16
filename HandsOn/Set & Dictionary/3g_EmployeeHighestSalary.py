n=int(input("Enter number of Employees:"))
d={}
for _ in range(n):
    key=input("Enter Employee name:")
    value=int(input("Enter Salary:"))
    d[key]=value
print(d)
highest=0
emp_highest_salary=""
for key,value in d.items():
    if value>highest:
        highest=value
        emp_highest_salary=key
print("The Employee with highest Salary is: ",emp_highest_salary)