from account import *

class Test:
    def setup_method(self):

        self.account_one = Account('Account1')
        self.account_two = Account('Account2')

    def teardown_method(self):

        del self.account_one
        del self.account_two

    def test_init(self):

        assert self.account_one.get_name() == "Account1"
        assert self.account_one.get_balance() == 0
        assert self.account_two.get_name() == "Account2"
        assert self.account_two.get_balance() == 0

    def test_deposit(self):

        assert self.account_one.deposit(1) is True
        assert self.account_one.get_balance() == 1.00
        assert self.account_two.get_balance() == 0.00
        assert self.account_one.deposit(-5) is False
        assert self.account_one.get_balance() == 1.00


    def test_withdraw(self):

        assert self.account_one.withdraw(1) is False
        assert self.account_one.get_balance() == 0.00
        assert self.account_two.get_balance() == 0.00

        self.account_one.deposit(5.00)
        assert self.account_one.withdraw(-5.00) is False
        assert self.account_one.get_balance() == 5.00
        assert self.account_one.withdraw(2.5) == True
        assert self.account_one.get_balance() == 2.5