class GYM_Base(type):
   _instances = {}
   def __call__(cls, *args, **kwargs):
       if cls not in cls._instances:
           cls._instances[cls] = super(GYM_Base, cls).\
               __call__(*args, **kwargs)
       return cls._instances[cls]

class GYM_Abonement(metaclass = GYM_Base):
    def __init__(self):
        self.name = "DayTime"

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str):
        self.name = name

if __name__ == "__main__":
    DayTime = GYM_Abonement()
    NightTime = GYM_Abonement()
    VIP = GYM_Abonement()
    print("Name_Abonements_First: " + DayTime.get_name())
    DayTime.set_name("NightTime")
    print("Name_Abonements_Second: " + NightTime.get_name())
    NightTime.set_name("VIP")
    print("Name_Abonements_Third: " + VIP.get_name())
    VIP.set_name("DayTimes")
    print("Name_Abonements_First_v_2.0: " + DayTime.get_name())
    print(DayTime)
    print(NightTime)
    print(VIP)
    print(DayTime)
    print(id(DayTime) == id(NightTime) == id(VIP) == id(DayTime))