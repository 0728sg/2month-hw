
class Asset:
    def __init__(self, value=0):
        self._value = value

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value

class InterestBearingItem(Asset):
    def __init__(self, value=0, interest_rate=0):
        super().__init__(value)
        self._interest_rate = interest_rate  
    def get_interest_rate(self):
        return self._interest_rate

    def set_interest_rate(self, interest_rate):
        self._interest_rate = interest_rate
class Security(Asset):
    pass

class Stock(Security):
    pass

class Bond(Security):
    pass

class RealEstate(Asset):
    def __init__(self, value=0, location=""):
        super().__init__(value)
        self._location = location

    def get_location(self):
        return self._location

    def set_location(self, location):
        self._location = location

class InsurableItem(RealEstate):
    def __init__(self, value=0, location="", insurance_value=0):
        super().__init__(value, location)
        self._insurance_value = insurance_value

    def get_insurance_value(self):
        return self._insurance_value

    def set_insurance_value(self, insurance_value):
        self._insurance_value = insurance_value

class BankAccount(Asset):
    def __init__(self, value=0, account_number=""):
        super().__init__(value)
        self._account_number = account_number

    def get_account_number(self):
        return self._account_number

    def set_account_number(self, account_number):
        self._account_number = account_number

class SavingAccount(BankAccount, InterestBearingItem):
    def __init__(self, value=0, account_number="", interest_rate=0):
        BankAccount.__init__(self, value, account_number)
        InterestBearingItem.__init__(self, value, interest_rate)
class CheckingAccount(BankAccount):
    pass
