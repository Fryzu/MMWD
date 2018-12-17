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
        settings.LINES_NUMBER = 3

        city = City()
        with open(os.path.join(project_dir, "test_city_15.json"), 'r') as r_file:
            city.importFromJson(r_file)
        solution = Solution()
        self.taboAlgo = TaboAlgo(city, solution)

    def test_iterate(self):
        settings.ITERATION = 1000
        bestLinesCost = self.taboAlgo.bestLinesCost
        bestLines = self.taboAlgo.bestLines
        n = 0
        while n <settings.ITERATION:
            n+=1
            print("Postęp: " + str(n*100/settings.ITERATION)+"%")
            self.taboAlgo.iterate()
        print("\nBefore iteration:")
        print("cost: ", bestLinesCost)
        print(bestLines)
        print("After iteration:")
        print("cost: ", self.taboAlgo.bestLinesCost)
        print(self.taboAlgo.bestLines)

if __name__== "__main__":
    unittest.main()
