from abc import ABC,abstractmethod
class Validator(ABC):
    @abstractmethod
    def validate(self,data):
        pass
class EmailValidator(Validator):
    def validate(self,data):
        if "@" in data and "." in data:
            return "Valid Email"
        return "Invalid Email"
class PasswordValidator(Validator):
    def validate(self,data):
        if len(data)>=8 and any(char.isdigit() for char in data):
            return "Valid PW"
        return "Invalid PW"

email=EmailValidator()
print(email.validate("anusuyasm322@gmail.com"))
pw=PasswordValidator()
print(pw.validate("Anu123"))

