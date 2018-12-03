import unittest
from Solution import Solution
from City import City
from TaboAlgo import TaboAlgo
import settings

import os #files and directories
project_dir = os.path.dirname(os.path.abspath(__file__))

class TestTaboAlgo(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        print("\nTabo algo test case\n======================")

        #initializing a test taboalgo
        city = City()
        with open(os.path.join(project_dir, "test_city.json"), 'r') as r_file:
            city.importFromJson(r_file)
        solution = Solution()
        with open(os.path.join(project_dir, "test_solution.json"), 'r') as r_file:
            solution.importFromJson(r_file)
        self.taboAlgo = TaboAlgo(city, solution)

    def test_cost_function(self):
        self.assertEqual(self.taboAlgo.cost(), 173)

    def test_iterate(self):
        pass

if __name__== "__main__":
    unittest.main()
