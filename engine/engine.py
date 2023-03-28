from abc import ABC, abstractmethod
from Interfaces.serviceable import Serviceable
from datetime import datetime

class Engine(Serviceable, ABC):
    def __init__(self, last_service_date) -> None:
        super().__init__(last_service_date)

class CapuletEngine(Engine):
    def __init__(self, current_mileage, last_service_mileage, last_service_date=datetime.now()):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 30000

    def service(self, date: datetime):
        self.last_service_mileage = 0
        self.last_service_date = date
    

class SternmanEngine(Engine):
    def __init__(self, warning_light_on: bool, last_service_date=datetime.now()):
        super().__init__(last_service_date)
        self.warning_light_on = warning_light_on

    def needs_service(self):
        if self.warning_light_on:
            return True
        else:
            return False
        
    def service(self, date: datetime):
        self.last_service_date = date
        self.warning_light_on = False
        

class WilloughbyEngine(Engine):
    def __init__(self, current_mileage, last_service_mileage, last_service_date=datetime.now()):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 60000
    
    def service(self, date: datetime):
        self.last_service_mileage = 0
        self.last_service_date = date


