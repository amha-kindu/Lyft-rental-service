from datetime import datetime

from Interfaces.serviceable import Serviceable


class Tires(Serviceable):
    def __init__(self, last_service_date=datetime.now()) -> None:
        super().__init__(last_service_date)
        self.tires = [0, 0, 0, 0]
    
    def service(self):
        self.tires = [0]*4

class CarriganTires(Tires):
    def needs_service(self) -> bool:
        return len(list(filter(lambda x: x >= 0.9, self.tires))) > 0
    
class Octoprime(Tires):
    def needs_service(self) -> bool:
        return sum(self.tires) >= 3
