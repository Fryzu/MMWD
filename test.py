import unittest
from structures import *

class TestStructures(unittest.TestCase):
    def test_city_creation(self):
        city = City()
        # print(city.printDistance())
        # print(city.printTraffic())
    def test_get_distance(self):
        city = City()
        for i in range(0, MAP_SIZE):
            for j in range(0, MAP_SIZE):
                self.assertEqual(city._conncections[i][j]["distance"], city.getDistance(i, j)) 
    def test_get_traffic(self):
        city = City()
        for i in range(0, MAP_SIZE):
            for j in range(0, MAP_SIZE):
                self.assertEqual(city._conncections[i][j]["traffic"], city.getTraffic(i, j)) 
    def test_solution_creation(self):
        solution = Solution(None)
        # print(solution)
    def test_value_function(self):
        city = City()
        solution = Solution(city)
        print(city.printTraffic())
        print(solution.value)


if __name__== "__main__":
    unittest.main()