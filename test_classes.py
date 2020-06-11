#!/usr/bin/env python
import unittest
import sys
sys.path.append('/Users/Caetan/Desktop/PP/Practicas/python2020')
import task2


# python3 test_task2.py

# ###########################
# # UNIT TESTS
# ###########################

class AircraftTests(unittest.TestCase):
    def setUp(self):
        # This will run before each test case
        self.task2_aircraft1 = task2.Aircraft("Spanair", "McDonnell Douglas MD-82", "EC-HFP", "53148/2072")
        self.task2_aircraft2 = task2.Aircraft("?", "?", "?", "?/2072")
    
    def test_flight_type(self):
        result = self.task2_aircraft1.get_type()
        self.assertEqual(result, 'Commercial')
        
    def test_flight_fl(self):
        result = self.task2_aircraft2.get_fl()
        self.assertEqual(result, '2072')
        
    def tearDown(self):
        # This will run after each test case
        pass

class CrashTests(unittest.TestCase):
    def setUp(self):
        # This will run before each test case
        a1 = task2.Aircraft("Spanair", "McDonnell Douglas MD-82", "EC-HFP", "53148/2072")
        self.task2_crash1 = task2.Crash(a1, "West Germany", "5022")
        self.task2_crash2 = task2.Crash(a1, "?", "?")
    
    def test_flight_company(self):
        result = self.task2_crash1.company
        self.assertEqual(result, 'Spanair')
        
    def test_flight_location(self):
        result = self.task2_crash2.location
        self.assertEqual(result, '?')
        
    def tearDown(self):
        # This will run after each test case
        pass


class VictimsTests(unittest.TestCase):
    def setUp(self):
        # This will run before each test case
        a1 = task2.Aircraft("Spanair", "McDonnell Douglas MD-82", "EC-HFP", "53148/2072")
        c1 = task2.Crash(a1, "West Germany", "5022")
        c2 = task2.Crash(a1, "?", "?")
        self.task2_victims1 = task2.Victims(c1, "76 (passengers:60 crew:16)", "30 (passengers:15 crew:15)", "3")
        self.task2_victims2 = task2.Victims(c1, "76 (passengers:? crew:16)", "30 (passengers:15 crew:?)", "3")
        self.task2_victims3 = task2.Victims(c1, "? (passengers:? crew:16)", "30 (passengers:? crew:?)", "?")
        self.task2_victims4 = task2.Victims(c2, "?", "?", "?")
        self.task2_victims5 = task2.Victims(c1, "76 (passengers:50 crew:?)", "30 (passengers:15 crew:?)", "3")
    
    def test_flight_victims1(self):
        result = self.task2_victims1.victims_role()
        self.assertEqual(result, ('76', '60', '16', '30', '15', '15', '3'))
        
    def test_flight_victims2(self):
        result = self.task2_victims2.victims_role()
        self.assertEqual(result, ('76', 'UNKNOWN', '16', '30', '15', 'UNKNOWN', '3'))

    def test_flight_victims3(self):
        result = self.task2_victims3.victims_role()
        self.assertEqual(result, ('UNKNOWN', 'UNKNOWN', '16', '30', 'UNKNOWN', 'UNKNOWN', '?'))

    def test_flight_victims4(self):
        result = self.task2_victims4.victims_role()
        self.assertIsNone(result)

    def test_flight_victims5(self):
        result = self.task2_victims5.victims_role()
        self.assertEqual(result, ('76', '50', 'UNKNOWN', '30', '15', 'UNKNOWN', '3'))

    def test_alive_passengers1(self):
        result = self.task2_victims1.alive_passengers()
        self.assertEqual(result, 45)
        
    def test_alive_passengers2(self):
        result = self.task2_victims2.alive_passengers()
        self.assertIsNone(result)

    def test_alive_passengers3(self):
        result = self.task2_victims3.alive_passengers()
        self.assertIsNone(result)

    def test_alive_passengers4(self):
        result = self.task2_victims4.alive_passengers()
        self.assertIsNone(result)
     
    def test_alive_passengers5(self):
        result = self.task2_victims5.alive_passengers()
        self.assertEqual(result, 35)

    def test_alive_crew1(self):
        result = self.task2_victims1.alive_crew()
        self.assertEqual(result, 1)
        
    def test_alive_crew2(self):
        result = self.task2_victims2.alive_crew()
        self.assertIsNone(result)

    def test_alive_crew3(self):
        result = self.task2_victims3.alive_crew()
        self.assertIsNone(result)

    def test_alive_crew4(self):
        result = self.task2_victims4.alive_crew()
        self.assertIsNone(result)

    def test_alive_crew5(self):
        result = self.task2_victims5.alive_crew()
        self.assertIsNone(result)

    def tearDown(self):
        # This will run after each test case
        pass


if __name__ == '__main__':
    unittest.main()