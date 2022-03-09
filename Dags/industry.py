import time


>>>>>>> Stashed changes
class IndustryAmountError(TypeError):
    """Amount must be at least 0"""
    pass


class Balance:
    def __init__(self, uid: int, amount: float):
        """
        :param int uid: Unique ID счета
        :param float amount: Остаток на счете
        """
        if not isinstance(uid, int): raise TypeError("UID must be integer")
        if not (isinstance(amount, int) or isinstance(amount, float)): raise TypeError("Amount must be integer or float")
        self.__uid, self.__amount = uid, amount

    def get_uid(self):
        return self.__uid

    def get_amount(self):
        return self.__amount

    def set_amount(self, new_amount: float):
        if not (isinstance(new_amount, float) or isinstance(new_amount, int)):
            raise IndustryAmountError("Amount must be integer or float")
        if new_amount < 0:
            raise IndustryAmountError('Amount must be at least 0')
        self.__amount = new_amount


class IndustryHandler:
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
            raise IndustryAmountError("Amount must be integer or float")
        new_value_a = self.account_a.get_amount() - amount
        new_value_b = self.account_b.get_amount() + amount

        self.account_a.set_amount(new_value_a)
        self.account_b.set_amount(new_value_b)


class Pack:
    def __init__(self, material: str, volume: float, height: float, shape: str, expiration: int):
        self.material = material
        self.volume = volume
        self.height = height
        self.shape = shape
        self.expiration = expiration

    pass


class Product:
    def __init__(self, weight: float, expiration_date: float, recommended_temperature: float,
                 current_temperature: float):
        self.weight = weight
        self.expiration_date = expiration_date
        self.recommended_temperature = recommended_temperature
        self.current_temperature = current_temperature

    pass


class Milk(Product):
    def __init__(self, fat_content: float, pasteurization: str, weight: float, expiration_date: float, recommended_temperature: float, current_temperature: float):
        super().__init__(weight, expiration_date, recommended_temperature, current_temperature)
        self.fat_content = fat_content
        self.pasteurization = pasteurization

    def pasteurizationM(self):
        time.sleep(2)
        self.pasteurization = 'sterilized'
        self.expiration_date += 3

    def pasteurizationF(self):
        time.sleep(10)
        self.pasteurization = 'pasteurized'
        self.expiration_date += 7

    def pasteurizationL(self):
        time.sleep(20)
        self.pasteurization = 'ultra - pasteurized'
        self.expiration_date += 14

    def info(self):
        print("pasteurization:", self.pasteurization)
        print("fats:", str(self.fat_content) + "%")
        print("expiration date:", self.expiration_date)
        print("recommended temperature:", self.recommended_temperature)
        print("current temperature:", self.current_temperature)

    pass


if __name__ == '__main__':
    vasya = Account(uid=1, amount=500)
    petya = Account(uid=1, amount=5000)
    handler = IndustryHandler(vasya, petya)
    pack = Pack('cardboard', 1, 0.3, 'oval', 20)
    product = Product(1, 30, 25, 18)
    milk = Milk(9, 25, 50, 28, 12, 12)

    print(vasya.get_amount(), petya.get_amount())
    handler.transfer(100)
    print(vasya.get_amount(), petya.get_amount())
    handler.transfer(-1000)
    print(vasya.get_amount(), petya.get_amount())
    print(milk.info())
    milk.pasteurizationM()
    print(milk.info())
