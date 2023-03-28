from Interfaces.serviceable import Serviceable
from battery.battery import Battery
from engine.engine import *
from tires.tires import Tires



class Car(object):
    def __init__(self, engine: Engine, battery: Battery, tires: Tires):
        self.engine = engine
        self.battery = battery
        self.tires = tires

    def needs_service(self):
        return self.engine.needs_service() or \
                self.battery.needs_service() or \
                self.tires.needs_service()

    def service(self):
        date = datetime.now()
        if self.engine.needs_service():
            self.engine.service(date)
        if self.battery.needs_service():
            self.battery.service(date)
        if self.tires.needs_service():
            self.tires.service(date)
    
    def replace_battery(self, new_battery: Battery) -> bool:
        self.battery = new_battery
 
