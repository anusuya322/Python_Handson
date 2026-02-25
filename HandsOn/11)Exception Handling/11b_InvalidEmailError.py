class InvalidEmailError(Exception):
    pass
try:
    email=input("Enter your email address:")
    if "@" not in email:
        raise InvalidEmailError("Email does not contain @")
    print("Valid email with @")
except InvalidEmailError as e:
    print("Error:",e)
