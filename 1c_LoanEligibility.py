income=int(input("Enter your income:"))
credit_score=int(input("Enter your credit score:"))
debt=int(input("Enter your existing debt amount:"))
DI_ratio=(debt/income)*100
if credit_score>=750 and DI_ratio<40:
    print("Eligible for loan")
elif 650<=credit_score<750 and DI_ratio<50:
    print("Review for loan")
else:
    print("Rejected for loan")
