import unittest
from Solution import Solution
from City import City
from TaboAlgo import TaboAlgo
import settings

class TestTaboAlgo(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        print("\nTabo algo test case\n======================")

        #initializing a test taboalgo
        city = City()
        with open('C:/Users/Sylwester/PycharmProjects/MMWDd/tests/test_city.json', 'r') as r_file:
            city.importFromJson(r_file)
        solution = Solution()
        with open('C:/Users/Sylwester/PycharmProjects/MMWDd/tests/test_solution.json', 'r') as r_file:
            solution.importFromJson(r_file)
        print("\nSoluion test case:\n======================")
        print(solution)
        print("City test case:\n======================")
        print(city.printDistance())
        print(city.printTraffic())
        settings.TABUTIME = 2
        self.taboAlgo = TaboAlgo(city, solution)
        print(self.taboAlgo.iterate())
    def test_cost_function(self):
        pass## self.assertEqual(self.taboAlgo.cost, 173)

    def iterate(self):
        pass

if __name__== "__main__":
    unittest.main()
