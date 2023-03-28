import unittest
from datetime import datetime

import sys, os

sys.path.insert(0, os.getcwd())

from battery.battery import Battery, NubbinBattery, SpindlerBattery
from car.car import Car
from engine.engine import CapuletEngine, SternmanEngine, WilloughbyEngine

class TestCalliope(unittest.TestCase):

    def test_battery_should_be_serviced(self):
        today = datetime.now()
        last_service_date = datetime.now().replace(year=today.year - 3)

        calliope_car = Car(
            engine=CapuletEngine(0, 0), 
            battery=SpindlerBattery(last_service_date=last_service_date)
        )

        self.assertTrue(calliope_car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.now()
        last_service_date = today.replace(year=today.year - 1)

        calliope_car = Car( 
            engine=CapuletEngine(0, 0), 
            battery=SpindlerBattery(last_service_date=last_service_date)
        )

        self.assertFalse(calliope_car.needs_service())

    def test_engine_should_be_serviced(self):
        calliope_car = Car(
            engine=CapuletEngine(current_mileage=30001, last_service_mileage=0),
            battery=SpindlerBattery()
        )
        self.assertTrue(calliope_car.needs_service())

    def test_engine_should_not_be_serviced(self):
        calliope_car = Car(
            engine=CapuletEngine(current_mileage=30000, last_service_mileage=0),
            battery=SpindlerBattery()
        )
        self.assertFalse(calliope_car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):

        today = datetime.now()
        last_service_date = today.replace(year=today.year - 3)

        glissade_car = Car(
            engine=WilloughbyEngine(0, 0), 
            battery=SpindlerBattery(last_service_date=last_service_date)
        )

        self.assertTrue(glissade_car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.now()
        last_service_date = today.replace(year=today.year - 1)

        glissade_car = Car(
            engine=WilloughbyEngine(0, 0), 
            battery=SpindlerBattery(last_service_date=last_service_date)
        )

        self.assertFalse(glissade_car.needs_service())

    def test_engine_should_be_serviced(self):
        glissade_car = Car(
            engine=WilloughbyEngine(60001, 0), 
            battery=SpindlerBattery()
        )
        self.assertTrue(glissade_car.needs_service())

    def test_engine_should_not_be_serviced(self):
        glissade_car = Car(
            engine=WilloughbyEngine(60000, 0), 
            battery=SpindlerBattery()
        )
        self.assertFalse(glissade_car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):

        today = datetime.now()
        last_service_date = today.replace(year=today.year - 5)

        palindrome_car = Car(
            engine=SternmanEngine(False, last_service_date),
            battery=SpindlerBattery(last_service_date)
        )

        self.assertTrue(palindrome_car.needs_service())


    def test_battery_should_not_be_serviced(self):
        today = datetime.now()
        last_service_date = today.replace(year=today.year - 1)

        palindrome_car = Car(
            engine=SternmanEngine(False, last_service_date), 
            battery=SpindlerBattery(last_service_date)
        )

        self.assertFalse(palindrome_car.needs_service())

    def test_engine_should_be_serviced(self):
        palindrome_car = Car(
            engine=SternmanEngine(True), 
            battery=SpindlerBattery()
        )
        
        self.assertTrue(palindrome_car.needs_service())


    def test_engine_should_not_be_serviced(self):
        palindrome_car = Car(
            engine=SternmanEngine(False), 
            battery=SpindlerBattery()
        )
        
        self.assertFalse(palindrome_car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):

        today = datetime.now()
        last_service_date = today.replace(year=today.year - 5)

        rorschach_car = Car(
            engine=WilloughbyEngine(0, 0), 
            battery=NubbinBattery(last_service_date)
        )

        self.assertTrue(rorschach_car.needs_service())


    def test_battery_should_not_be_serviced(self):
        today = datetime.now()
        last_service_date = today.replace(year=today.year - 3)

        rorschach_car = Car(
            engine=WilloughbyEngine(0, 0), 
            battery=NubbinBattery(last_service_date)
        )

        self.assertFalse(rorschach_car.needs_service())

    def test_engine_should_be_serviced(self):
        rorschach_car = Car(
            engine=WilloughbyEngine(60001, 0), 
            battery=NubbinBattery()
        )
        
        self.assertTrue(rorschach_car.needs_service())

    def test_engine_should_not_be_serviced(self):
        rorschach_car = Car(
            engine=WilloughbyEngine(60000, 0), 
            battery=NubbinBattery()
        )
        
        self.assertFalse(rorschach_car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.now()
        last_service_date = today.replace(year=today.year - 5)

        thovex_car = Car(
            engine=CapuletEngine(0, 0), 
            battery=NubbinBattery(last_service_date)
        )

        self.assertTrue(thovex_car.needs_service())


    def test_battery_should_not_be_serviced(self):
        today = datetime.now()
        last_service_date = today.replace(year=today.year - 3)

        thovex_car = Car(
            engine=CapuletEngine(0, 0, today), 
            battery=NubbinBattery(last_service_date)
        )

        self.assertFalse(thovex_car.needs_service())

    def test_engine_should_be_serviced(self):
        thovex_car = Car(
            engine=CapuletEngine(current_mileage=30001, last_service_mileage=0), 
            battery=NubbinBattery()
        )
        
        self.assertTrue(thovex_car.needs_service())

    def test_engine_should_not_be_serviced(self):
        thovex_car = Car(
            engine=CapuletEngine(current_mileage=30000, last_service_mileage=0), 
            battery=NubbinBattery()
        )
        
        self.assertFalse(thovex_car.needs_service())


if __name__ == '__main__':
    unittest.main()
