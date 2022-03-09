
class BankAmountError(TypeError):
    """Amount must be at least 0"""
    pass


class Account:
    def __init__(self, uid: int, amount: float, is_active: bool):
        """
        :param int uid: Unique ID счета
        :param float amount: Остаток на счете
        :param bool is_active:
        """
        # TODO: Add UID validation
        if not isinstance(uid, int): raise TypeError("UID must be integer")
        if not (isinstance(amount, int) or isinstance(amount, float)): raise TypeError("Amount must be integer or float")
        if not isinstance(is_active, bool): raise TypeError("IsActive must be integer")
        self.__uid, self.__amount, self.is_active = uid, amount, is_active

    def get_uid(self):
        return self.__uid

    def get_amount(self):
        return self.__amount

    def set_amount(self, new_amount: float):
        if not (isinstance(new_amount, float) or isinstance(new_amount, int)):
            raise BankAmountError("Amount must be integer or float")
        if new_amount < 0:
            raise BankAmountError('Amount must be at least 0')
        self.__amount = new_amount


class BankHandler:
    """
    Provides transfer from account A to account B
    """
    def __init__(self, account_a: Account, account_b: Account):
        if not (isinstance(account_a, Account) and isinstance(account_b, Account)):
            raise TypeError("AccountA and AccountB must be Account")
        self.account_a = account_a
        self.account_b = account_b

    def transfer(self, amount: float):
        if not (isinstance(amount, int) or isinstance(amount, float)):
            raise BankAmountError("Amount must be integer or float")
        new_value_a = self.account_a.get_amount() - amount
        new_value_b = self.account_b.get_amount() + amount

        self.account_a.set_amount(new_value_a)
        self.account_b.set_amount(new_value_b)


if __name__ == '__main__':
    vasya = Account(uid=1,
                    amount=500,
                    is_active=True)
    petya = Account(uid=1,
                    amount=5000,
                    is_active=True)

    handler = BankHandler(vasya, petya)

    print(vasya.get_amount(), petya.get_amount())
    handler.transfer(100)
    print(vasya.get_amount(), petya.get_amount())
    handler.transfer(-1000)
    print(vasya.get_amount(), petya.get_amount())
