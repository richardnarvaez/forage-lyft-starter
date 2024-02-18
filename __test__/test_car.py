import unittest
from datetime import datetime

from car.car_factory import CarFactory

class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0
        tires = [0.1, 0.2, 0.3, 0.5]

        calliope_car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, tires)
        self.assertTrue(calliope_car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        tires = [0.1, 0.2, 0.3, 0.5]

        calliope_car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, tires)
        self.assertFalse(calliope_car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        tires = [0.1, 0.2, 0.3, 0.5]

        calliope_car = CarFactory.create_calliope(datetime.today().date(), last_service_date, current_mileage, last_service_mileage, tires)
        self.assertTrue(calliope_car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tires = [0.1, 0.2, 0.3, 0.5]    

        calliope_car = CarFactory.create_calliope(datetime.today().date(), last_service_date, current_mileage, last_service_mileage, tires)
        self.assertFalse(calliope_car.needs_service())

if __name__ == '__main__':
    unittest.main()
