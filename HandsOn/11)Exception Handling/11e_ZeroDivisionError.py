try:
    num1=int(input("Enter a number1:"))
    num2=int(input("Enter a number2:"))
    if num2==0:
        raise ZeroDivisionError
    else:
        print(num1/num2)
except ZeroDivisionError:
    print("Error: Denominator cannot be zero")
except ValueError:
    print("Invalid Input")