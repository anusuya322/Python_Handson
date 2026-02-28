import re
inp_str=input("Enter your input:")
pattern=r"^\d{4}-\d{2}-\d{2}"
if re.match(pattern,inp_str):
    print("Valid input")
else:
    print("Invalid input")