from abc import ABC, abstractmethod

class IGYM_Abonement(ABC):
    @abstractmethod
    def cost(self) -> float:
        pass

class GYM_Abonement(IGYM_Abonement):
   def __init__(self, cost):
       self.__cost = cost

   def cost(self) -> float:
       return self.__cost

class IDecorator(IGYM_Abonement):
    @abstractmethod
    def name(self) -> str:
        pass

class DayTime(IDecorator):

    def __init__(self, wrapped: IGYM_Abonement, day_abonement_cost: float):
         self.__wrapped = wrapped
         self.__cost = day_abonement_cost
         self.__name = "DayTime"

    def cost(self) -> float:
         return self.__cost + self.__wrapped.cost()

    def name(self) -> str:
         return self.__name

class NightTime(IDecorator):

    def __init__(self, wrapped: IGYM_Abonement, night_abonement_cost: float):
        self.__wrapped = wrapped
        self.__cost = night_abonement_cost
        self.__name = "NightTime"

    def cost(self) -> float:
            return (self.__cost + self.__wrapped.cost())

    def name(self) -> str:
            return self.__name

if __name__ == "__main__":
     def print_abonement(abonement: IDecorator) -> None:
         print(f"Стоимость абонемента '{abonement.name()}' = {abonement.cost()} ")

     abonement_base = GYM_Abonement(100)
     print(f"Стоимость места в тренажерном зале = {abonement_base.cost()}")
     DayTime = DayTime(abonement_base, 900)
     print_abonement(DayTime)
     NightTime = NightTime(abonement_base, 800)
     print_abonement(NightTime)