from Interfaces.serviceable import Serviceable
from battery.battery import Battery
from engine.engine import *



class Car(object):
    def __init__(self, engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()

    def service(self):
        date = datetime.now()
        if self.engine.needs_service():
            self.engine.service(date)
        if self.battery.needs_service():
            self.battery.service(date)
    
    def replace_battery(self, new_battery: Battery) -> bool:
        self.battery = new_battery
 
