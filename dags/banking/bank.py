import json


# TODO: REMOVE PLUGS
# from airflow.models import Variable

class VariablePlug:
    def __init__(self):
        self.variables = {
            'transaction_commission': 0.02,
            'incoming_transactions': [], # UIDFrom, UIDTo, Amount
            'outgoing_transactions': [],
        }

    def get(self, key, default_var=None, deserialize_json=False):
        value = self.variables.get(key, default_var)
        if deserialize_json:
            value = json.loads(value)
        return value

    def set(self, key, value):
        self.variables[key] = value
    pass


#Variable = VariablePlug()
from airflow.models import Variable
# ----------------------------------------------------------------------------------------------------------------


class BankError(Exception): pass
class BankAccountError(BankError): pass


class Account:
    def __init__(self, uid: int, is_active: bool) -> None:
        """
        :param int uid: Unique ID счета
        :param bool is_active:
        """
        # TODO: Add UID validation
        if not isinstance(uid, int):
            raise TypeError("UID must be integer")
        if not isinstance(is_active, bool):
            raise TypeError("IsActive must be integer")
        self.__uid, self.__is_active = uid, is_active

    def get_uid(self) -> int:
        return self.__uid

    def get_balance(self) -> float:
        incoming = Variable.get('incoming_transactions', default_var=[])
        outgoing = Variable.get('outgoing_transactions', default_var=[])

        incoming_filtered = filter(lambda x: x[1] == self.__uid, incoming)
        outgoing_filtered = filter(lambda x: x[1] == self.__uid, outgoing)
        balance = sum(map(lambda x: x[2], incoming_filtered)) - sum(map(lambda x: x[2], outgoing_filtered))
        return balance

    def commit_transaction(self, from_account_uid, balance: float) -> None: #TODO:
        if not self.__is_active:
            raise BankAccountError("Account isn't active")
        if not (isinstance(balance, float) or isinstance(balance, int)):
            raise BankAccountError("Balance must be integer or float")
        if not balance:
            return
        transaction = (from_account_uid, self.get_uid(), abs(balance))

        incoming = Variable.get('incoming_transactions', default_var=[])
        outgoing = Variable.get('outgoing_transactions', default_var=[])

        if balance > 0:
            incoming.append(transaction)
            Variable.set('incoming_transactions', incoming)
        else:
            outgoing.append(transaction)
            Variable.set('outgoing_transactions', outgoing)


    pass


class Bank:
    @staticmethod
    def get_commission() -> float:
        return Variable.get('transaction_commission', 0)

    @staticmethod
    def load_account(uid):
        return Account(uid=uid, is_active=True)

    def __init__(self) -> None:
        self.bank_uid = Variable.get('bank_uid', default_var=1)
        self.accounts = [self.load_account(self.bank_uid)]
        self.accounts[0].commit_transaction(0,1000)
    '''
    def _create_account(self, i) -> int:
        uid = i
        new_account = Account(uid=uid,
                              is_active=True)
        self.accounts.append(new_account)
        return uid
    '''
    def get_account(self, uid: int) -> Account:
        """
        :param int uid:
        """
        if not isinstance(uid, int):
            raise TypeError("UID must be integer")

        account = list(filter(lambda x: x.get_uid() == uid, self.accounts))
        if not account:
            raise BankError('No such account')
        return account[0]

    def get_bank_account(self) -> Account:
        return self.get_account(self.bank_uid)

    '''
    def close_account(self, uid: int) -> tuple[bool, str]:
        if not isinstance(uid, int): raise TypeError("UID must be integer")
        try:
            account = self.get_account(uid)
            if account.get_balance() != 0:
                return False, "Account is not empty"
            self.accounts.remove(account)
            return True, ""
        except BankError as err:
            return False, str(err)
    '''
    pass


class BankHandler:
    """
    Provides transfer from account A to account B
    """

    def __init__(self, account_a: Account, account_b: Account) -> None:
        if not (isinstance(account_a, Account) and isinstance(account_b, Account)):
            raise TypeError("AccountA and AccountB must be Account")
        self.account_a = account_a
        self.account_b = account_b

    def transfer(self, amount: float, with_fee=True) -> None:
        if not isinstance(with_fee, bool):
            raise TypeError("with_fee must be boolean")
        if not (isinstance(amount, int) or isinstance(amount, float)):
            raise BankAccountError("Balance must be integer or float")
        if amount < 0:
            raise BankAccountError("Amount must be >= 0")

        bank = Variable.get('bank')

        fee = 0
        if with_fee:
            fee = bank.get_commission() * amount
            bank_account = bank.get_bank_account()

        new_value_a = -amount
        new_value_b = (amount-fee)

        self.account_a.commit_transaction(self.account_b.get_uid(), new_value_a)
        self.account_b.commit_transaction(self.account_a.get_uid(), new_value_b)
        if with_fee:
            bank_account.commit_transaction(self.account_a.get_uid(), fee)
    pass


def main():
    bank = Bank()
    Variable.set('bank', bank)  # TODO: make sure that it'll take a ride

    a_account_uid = bank._create_account()
    a_account = bank.get_account(a_account_uid)
    handler = BankHandler(bank.get_bank_account(), a_account)
    handler.transfer(100, with_fee=False)

    b_account_uid = bank._create_account()
    b_account = bank.get_account(b_account_uid)
    handler = BankHandler(bank.get_bank_account(), b_account)
    handler.transfer(100, with_fee=False)
    print(a_account.get_balance(), b_account.get_balance(), bank.get_bank_account().get_balance())

    handler = BankHandler(a_account, b_account)
    handler.transfer(50)

    print(a_account.get_balance(), b_account.get_balance(), bank.get_bank_account().get_balance())
    print(bank.get_account(1))

    incoming = Variable.get('incoming_transactions', default_var=[])
    outgoing = Variable.get('outgoing_transactions', default_var=[])
    print(incoming, outgoing)
    pass


if __name__ == '__main__':
    main()
