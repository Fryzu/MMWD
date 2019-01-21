import unittest
from Solution import Solution
from City import City
from TaboAlgo import TaboAlgo
import settings
import json

#import pandas as pd
import matplotlib.pyplot as plt
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
        settings.TABUTIME = 40

        city = City()
        with open(os.path.join(project_dir, "test_city_15.json"), 'r') as r_file:
            city.importFromJson(r_file)
        solution = Solution()
        #solution.updateLines([[14, 12, 11, 10, 7], [2, 4, 9, 13, 14], [2, 3, 5, 8, 12]])
        self.taboAlgo = TaboAlgo(city, solution)

    def test_iterate(self):
        bestLinesCost = self.taboAlgo.bestLinesCost
        bestLines = self.taboAlgo.bestLines
        settings.ITERATION = 1000
        costRun = []
        i = 0
        print('\n')
        print("|Postęp:  |", flush=True)
        while i < settings.ITERATION:
            i=i+1
            self.taboAlgo.iterate()
            costRun.append(self.taboAlgo.actualCost)
            if (i*10/settings.ITERATION) % 1 == 0:
                print("=", end='', flush=True)


        print("\nBefore iteration:")
        print("cost: ", bestLinesCost)
        print(bestLines)
        print("After iteration:")
        print("cost: ", self.taboAlgo.bestLinesCost)
        print(self.taboAlgo.bestLines)
        print(self.taboAlgo.city.printDistance())
        print(self.taboAlgo.city.printTraffic())
        plt.plot(range(settings.ITERATION), costRun)
        plt.grid()
        plt.show()


if __name__== "__main__":
    unittest.main()
