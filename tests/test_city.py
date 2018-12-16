import unittest
from City import City
import settings

import os #files and directories
project_dir = os.path.dirname(os.path.abspath(__file__))

class TestCity(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.city = City()

        #imports test_file.json and loads it to the city
        with open(os.path.join(project_dir, "test_city.json"), 'r') as r_file:
            self.city.importFromJson(r_file)

        print("City test case:\n======================")
        print(self.city.printDistance())
        print(self.city.printTraffic())

    def test_json(self):
        expectedJson = """[[{"distance":Infinity,"traffic":Infinity},{"distance":5,"traffic":7},{"distance":10,"traffic":5}],[{"distance":3,"traffic":4},{"distance":Infinity,"traffic":Infinity},{"distance":2,"traffic":3}],[{"distance":10,"traffic":10},{"distance":5,"traffic":1},{"distance":Infinity,"traffic":Infinity}]]"""
        actualJson = self.city.exportToJson().replace(" ","").replace("\n","")

        self.assertEqual(actualJson, expectedJson)

    def test_getters(self):
        self.assertEqual(self.city.getDistance(1, 2), 2)
        self.assertEqual(self.city.getTraffic(1, 2), 3)

    def test_size_15(self):
        settings.MAP_SIZE = 15
        c = City()
        with open(os.path.join(project_dir, "test_city_15.json"), 'r') as r_file:
            c.importFromJson(r_file)

        print("\nCity test 15 size:\n======================")
        print(c.printDistance())
        print(c.printTraffic())
        settings.MAP_SIZE = 3

if __name__== "__main__":
    unittest.main()
