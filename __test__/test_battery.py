import unittest
from datetime import datetime

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = datetime(2024, 2, 18)
        last_service_date = datetime(2020, 2, 17)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = datetime(2024,5,20)
        last_service_date = datetime(2023, 4, 20)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())

class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = datetime(2024, 2, 18)
        last_service_date = datetime(2020, 4, 20)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = datetime(2024, 2, 18)
        last_service_date = datetime(2023,2, 19)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()
