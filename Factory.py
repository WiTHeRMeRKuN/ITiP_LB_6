from enum import Enum

class NameAbonements(Enum):
    DayTime = 0,
    NightTime = 1,
    VIP = 2,

class Abonement:

    def __init__(self, price: float):
        self.__price = price

    def get_price(self) -> float:
        return self.__price


class Abonement_DayTime(Abonement):
    def __init__(self):
        super().__init__(1000)

class Abonement_NightTime(Abonement):
    def __init__(self):
        super().__init__(900)

class Abonement_VIP(Abonement):
    def __init__(self):
        super().__init__(2000)

def SaleAbonements(abonement_type: NameAbonements) -> Abonement:
    factory_dict = {
        NameAbonements.DayTime: Abonement_DayTime,
        NameAbonements.NightTime: Abonement_NightTime,
        NameAbonements.VIP: Abonement_VIP,
    }
    return factory_dict[abonement_type]()

if __name__ == '__main__':
    for Abonement in NameAbonements:
        abonements = SaleAbonements(Abonement)
        print(f' Тип абонемента: {Abonement}, цена: {abonements.get_price()}')