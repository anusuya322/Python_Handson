import re
email=input("Enter your email:")
parts=re.split(r'[@.]',email)
print(parts)
if len(parts)!=3:
    print("Invalid email")
else:
    username=parts[0]
    domain=parts[1]
    extension=parts[2]
    username_valid=re.fullmatch(r'[a-zA-Z0-9._]+',username)
    domain_valid=re.fullmatch(r'[a-zA-Z0-9]+',domain)
    extension_valid=re.fullmatch(r'[A-Za-z]{2,}', extension)
    if username_valid and domain_valid and extension_valid:
        print("Valid email")
    else:
        print("Invalid email")


