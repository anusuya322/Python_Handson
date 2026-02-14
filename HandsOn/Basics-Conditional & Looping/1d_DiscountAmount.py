amount=int(input("Enter the amount:"))
print("After discount")
if amount<1000:
    print("Final amount:",amount)
elif 1000<=amount<=4999:
    amount=amount-(0.05*amount)
    print("Final amount:",amount)
elif amount>=5000:
    amount=amount-(0.10*amount)
    print("Final amount:",amount)
