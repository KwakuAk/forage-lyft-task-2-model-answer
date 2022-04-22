import unittest
from datetime import datetime

from engine.sternman_engine import SternmanEngine
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine

class testSternmanEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        warning_light_is_on = True

        sternmanEngine = SternmanEngine(warning_light_is_on)
        self.assertTrue(sternmanEngine.needs_service())
    
    def test_engine_should_not_be_serviced(self):
        warning_light_is_on = False

        sternmanEngine = SternmanEngine(warning_light_is_on)
        self.assertFalse(sternmanEngine.needs_service())

class testCapuletEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0

        capuletEngine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(capuletEngine.needs_service())
    
    def test_engine_should_not_be_serviced(self):
        current_mileage = 29000
        last_service_mileage = 0

        capuletEngine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(capuletEngine.needs_service())

class testWilloughbyEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0

        willoughbyEngine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(willoughbyEngine.needs_service())
    
    def test_engine_should_not_be_serviced(self):
        current_mileage = 59005
        last_service_mileage = 0

        willoughbyEngine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(willoughbyEngine.needs_service())