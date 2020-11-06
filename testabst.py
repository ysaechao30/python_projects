from abc import ABC, abstractmethod
class phonebill(ABC):
    def amountPay(self, amount):
        print("Total amount paid: ", amount)
        @abstractmethod
        def payment(self, amount):
            pass

class DebitPay(phonebill):
    def payment(self, amount):
        print('You have credit of {} from your previous overpayment of $.02 '.format(amount))


obj = DebitPay()
obj.amountPay(".02")
obj.payment(".02")
