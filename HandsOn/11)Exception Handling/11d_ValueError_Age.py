def age_check(age):
    if age<18:
        raise ValueError("Your age is less than 18")
    return "Your age is Eligible"
try:
    age=int(input("Enter your age:"))
    print(age_check(age))
except ValueError as e:
    print("Error:",e)

