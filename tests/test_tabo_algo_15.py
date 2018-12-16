import unittest
from Solution import Solution
from City import City
from TaboAlgo import TaboAlgo
import settings

import os #files and directories
project_dir = os.path.dirname(os.path.abspath(__file__))

class TestTaboAlgo15(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        print("\nTabo algo test case\n======================")

        #initializing a test taboalgo
        settings.MAP_SIZE = 15
        settings.LINE_LENGTH = 5
        settings.LINES_NUMBER = 5

        city = City()
        with open(os.path.join(project_dir, "test_city_15.json"), 'r') as r_file:
            city.importFromJson(r_file)
        solution = Solution()
        self.taboAlgo = TaboAlgo(city, solution)

    def test_iterate(self):
        print("\nBefore iteration:")
        print("cost: ", self.taboAlgo.bestLinesCost)
        print(self.taboAlgo.bestLines)
        n = 0
        while n <10:
            n+=1
            self.taboAlgo.iterate()
        print("After iteration:")
        print("cost: ", self.taboAlgo.bestLinesCost)
        print(self.taboAlgo.bestLines)

if __name__== "__main__":
    unittest.main()
