class Vehicle:
    def __init__(self,brand,max_speed,mileage):
        self.brand=brand
        self.max_speed=max_speed
        self.mileage=mileage
class bus(Vehicle):
    pass
school_bus=bus("Volvo","180","20")
print("Brand:", school_bus.brand,"Max Speed:", school_bus.max_speed,"Mileage:",school_bus.mileage)