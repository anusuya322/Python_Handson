class Vehicle:
    def vehicle_type(self,v_type):
        self.v_type=v_type
    def show_type(self):
        return self.v_type
class Car(Vehicle):
    def fuel_type(self,fuel):
        self.fuel=fuel
    def show_fuel(self):
        return self.fuel
class ElectricCar(Car):
    def battery_type(self,battery):
        self.battery=battery
    def show_battery(self):
        return self.battery
elec=ElectricCar()
elec.vehicle_type("EV")
print(elec.show_type())
elec.fuel_type("CNG")
print(elec.show_fuel())



