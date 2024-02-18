import unittest

from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires

class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        # One or more 0.9 -> True
        arr_tire = [0.5, 0.9, 0.7, 0.89]
        tires = CarriganTires(arr_tire)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        # Any >= 0.9 -> False
        arr_tire = [0.35, 0.89, 0.899, 0.01]
        tires = CarriganTires(arr_tire)
        self.assertFalse(tires.needs_service())

    def test_needs_service_false(self):
        # arr_tires > 4 -> 
        arr_tire = [0.35, 0.89, 0.899, 0.01, 0.2]
        tires = CarriganTires(arr_tire)
        self.assertFalse(tires.needs_service())

class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_true(self):
        # Sum >= 3 -> True
        arr_tire = [0.9, 0.9, 0.9, 0.3]
        tires = OctoprimeTires(arr_tire)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        # Sum < 3 -> False
        arr_tire = [0.9, 0.9, 0.9, 0.2]
        tires = OctoprimeTires(arr_tire)
        self.assertFalse(tires.needs_service())