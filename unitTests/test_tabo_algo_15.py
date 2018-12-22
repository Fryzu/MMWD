import unittest
from Solution import Solution
from City import City
from TaboAlgo import TaboAlgo
import settings
import json

#import pandas as pd
#import matplotlib.pyplot as plt
#import numpy as np

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
        settings.ITERATION = 100

        city = City()
        with open(os.path.join(project_dir, "test_city_15.json"), 'r') as r_file:
            city.importFromJson(r_file)
        solution = Solution()
        solution.updateLines([[3, 4, 0, 1, 2], [9, 0, 1, 2, 3], [8, 4, 0, 1, 2]])
        self.taboAlgo = TaboAlgo(city, solution)

    def test_iterate(self):
        #<<<<<<< HEAD
        bestLinesCost = self.taboAlgo.bestLinesCost
        bestLines = self.taboAlgo.bestLines
        settings.ITERATION = 100
        costRun = []
        i = 0
        print('\n')
        while i < settings.ITERATION:
            i=i+1
            self.taboAlgo.iterate()
            costRun.append(self.taboAlgo.actualCost)
            print("Postęp: "+str(i*100/settings.ITERATION) +"%")
       #plt.plot(range(100), costRun)
       # plt.grid()
        #plt.show()
        #=======
#>>>>>>> 31c6e68475f6cbc1646280c4938d64172d13c449
        print("\nBefore iteration:")
        print("cost: ", bestLinesCost)
        print(bestLines)
        print("After iteration:")
        print("cost: ", self.taboAlgo.bestLinesCost)
        print(self.taboAlgo.bestLines)
        print(self.taboAlgo.city.printDistance())
        print(self.taboAlgo.city.printTraffic())


if __name__== "__main__":
    unittest.main()
