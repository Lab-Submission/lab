class Account():

    """
    A class representing a bank account object
    """
    def __init__(self, name: str) -> None:

        """
        Constructor for creating account
        :param name: Name for the account
        """

        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:

        """
        Method to deposit to account.
        :param amount: Amount of money to be deposited.
        :return: Returns True if the deposit is successful, False if not.
        """

        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True

    def withdraw(self, amount: float) -> bool:

        """
        Method to withdraw from account.
        :param amount: Amount of money to be withdrawn.
        :return: Returns True if the withdrawal is successful, False if not.
        """

        if amount > self.__account_balance or amount <= 0:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> float:

        """
        Method to return balance of account
        :return: Balance of account.
        """

        return self.__account_balance

    def get_name(self) -> float:

        """
        method to return name of account
        :return: Name of account.
        """

        return self.__account_name