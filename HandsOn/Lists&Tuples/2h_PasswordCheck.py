limits=3
password=["Anusuya14"]
while limits>0:
    pw=input("Enter your password:")
    if pw==password[0]:
        print("Correct password")
        print("Successful attempt")
        break
    else:
        limits-=1
        print("Wrong password")
        print("Try Again, Limits left:",limits)
if limits==0:
   print("Invalid password. Account locked, Try after some time")
