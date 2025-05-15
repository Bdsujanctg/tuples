
class Vehicle:
     def __init__(self, capacity):
        self.capacity = capacity

     def fare(self):
        return self.capacity * 100


class Bus(Vehicle):
    def __init__(self, capacity):
        super().__init__(capacity)

    def fare(self):
        base_fare = super().fare()
        maintenance_charge = base_fare * 0.10
        total_fare = base_fare + maintenance_charge
        return total_fare



bus = Bus(50)
print("Total Bus Fare: INR", bus.fare())
