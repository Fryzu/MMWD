import unittest
from structures import *

class TestStructures(unittest.TestCase):
    def test_city_creation(self):
        city = City()
        print(city)
        city.printDistance()
    def test_solution_creation(self):
        solution = Solution()
        print(solution)

if __name__== "__main__":
    unittest.main()