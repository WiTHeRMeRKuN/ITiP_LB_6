from abc import ABC, abstractmethod
from enum import Enum
from random import choice
from typing import List

class AbonementType(Enum):
    DayTime = 1
    NightTime = 2
    VIP = 3

class Abonement:
    abonement_id: int = 1

    def __init__(self, abonement_type: AbonementType):
        self.id = Abonement.abonement_id
        self.type = abonement_type
        Abonement.abonement_id += 1

    def __str__(self):
        return f"абонемент {self.type.name} (Заказ №{self.id}) "

class Observer(ABC):
    @abstractmethod
    def update(self, order_id: int):
        ...

class Subject(ABC):
    def __init__(self):
        self._observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self, order_id: int) -> None:
        for observer in self._observers:
            observer.update(order_id)

class GYM(Subject):
   def __init__(self):
       super().__init__()
       self.__abonement: List[Abonement] = []
       self.__finish_abonement: List[Abonement] = []

   def take_abonement(self, abonement:Abonement) -> None:
       print(f"Был куплен {abonement}")
       self.__abonement.append(abonement)

   def get_abonement(self, abonement_id: int) -> Abonement:
       abonement = None
       for it in self.__finish_abonement:
           if it.id == abonement_id:
              abonement = it
              break
       self.__finish_abonement.remove(abonement)
       return abonement

class Client(Observer):
    def __init__(self, name: str, administrator: GYM):
        self.__administrator = administrator
        self.__name = name
        self.abonement: Abonement = None

    def update(self, abonement_id: int) -> None:
        if self.abonement is not None:
           if abonement_id == self.abonement.id:
              self.__administrator.detach(self)

    def create_order(self) -> None:
        abonement_type = choice([AbonementType.DayTime,
                             AbonementType.NightTime,
                             AbonementType.VIP])
        self.abonement = Abonement(abonement_type)
        print(f"Клиент {self.__name} выбрал {self.abonement}")
        self.__administrator.attach(self)
        self.__administrator.take_abonement(self.abonement)

if __name__ == "__main__":
     names = ['Владислав', 'Дарья',
              'Николай', 'Татьяна']
     Organization = GYM()
     clients = [Client(name, Organization) for name in names]
     for client in clients:
         print("*"*50)
         client.create_order()
