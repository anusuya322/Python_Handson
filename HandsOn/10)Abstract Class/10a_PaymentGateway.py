from abc import ABC, abstractmethod
class PaymentGateway(ABC):
    @abstractmethod
    def pay(self,amt):
        pass
    @abstractmethod
    def refund(self,amt):
        pass
class CreditCard(PaymentGateway):
    def pay(self,amt):
        print(f"Paid {amt} by Credit card")
    def refund(self,amt):
        print(f"Refunded {amt} to credit card")
class UPI(PaymentGateway):
    def pay(self,amt):
        print(f"Paid {amt} by UPI")
    def refund(self,amt):
        print(f"Refunded {amt} to UPI app")
class DebitCard(PaymentGateway):
    def pay(self,amt):
        print(f"Paid {amt} by debit card")

c=CreditCard()
c.pay(500)
c.refund(200)
upi=UPI()
upi.pay(4800)
upi.refund(400)
deb=DebitCard()
