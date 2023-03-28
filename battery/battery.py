from datetime import datetime
from Interfaces.serviceable import Serviceable



class Battery(Serviceable):

    def __init__(self, last_service_date: datetime) -> None:
        super().__init__(last_service_date)

class SpindlerBattery(Battery):
    def __init__(self, last_service_date = datetime.now()) -> None:
        super().__init__(last_service_date)
    
    def needs_service(self) -> bool:
        today = datetime.now().date()
        return ( today.year - self.last_service_date.year ) >= 3
    
class NubbinBattery(Battery):
    def __init__(self, last_service_date = datetime.now()) -> None:
        super().__init__(last_service_date)
    
    def needs_service(self) -> bool:
        today = datetime.now().date()
        return ( today.year - self.last_service_date.year ) >= 4