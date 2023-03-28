from abc import ABC, abstractmethod



class Serviceable(ABC):
    def __init__(self, last_service_date) -> None:
        super().__init__()
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self) -> bool:
        pass
    
    def service(self, date) -> None:
        self.last_service_date = date

