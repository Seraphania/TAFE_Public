from abc import ABC, abstractmethod

# Advanced exercises
# These exercises are not mandatory.

# 1. Implement a payment system where a base class `Payment` has a method `authorise_transaction()`. Create different payment method classes like `CreditCardPayment`, `DebitCardPayment`, and `PayPalPayment`, each implementing the authorization method differently (that can just be a print statement for now).

class Payment(ABC):
    """
    Define what a payment class should be able to do
    """
    @abstractmethod
    def authorise_transaction(self):
        pass

class CreditCardPayment(Payment):    
    def authorise_transaction(self): # Just a warning that I am overriding (inconsistently).
        return type(self).__name__ # better approach no side effects
    
class DebitCardPayment(Payment):
    def authorise_transaction(self):
        print(f"Your {type(self).__name__} payment has been authorised") # not ideal, better to return
        # is better to have consistent return types if using polymorphism

class PayPalPayment(Payment):
    def authorise_transaction(self):
        pass # kinda useless, but works.


#    1. Demonstrate that you can authorise transactions without any knowledge of the specific payment method.
ccp = CreditCardPayment()
receipt = ccp.authorise_transaction()
print(f"Your {receipt} is authorised")

dcp = DebitCardPayment()
dcp.authorise_transaction()

ppp = PayPalPayment()
ppp.authorise_transaction()
print(f"{type(ppp).__name__} payment authorised")

#    2. What would be the benefits of implementing `authorise_transaction` as an abstract method in the `Payment` class?
# This specifies that any subclass of the payemnt type must be able to authorise payments, but that this can be implemented in different ways.
# Ideally, the return types would be consisitent - not done above to illustrate inconsistency.

