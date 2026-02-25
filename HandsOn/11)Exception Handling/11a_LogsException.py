try:
    name=input("Enter your name:")
    if name.isdigit():
        raise ValueError("Name can't be numeric")
    print("Welcome",name)
except Exception as e:
    with open("errorlog.txt","a") as f:
        f.write(str(e)+"\n")
    print("Invalid input")