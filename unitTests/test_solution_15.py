import unittest
from Solution import Solution

import os #files and directories
project_dir = os.path.dirname(os.path.abspath(__file__))

class TestSolution(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.solution = Solution()

        #imports test_file.json and loads it to the solution
        with open(os.path.join(project_dir, "test_solution.json"), 'r') as r_file:
            self.solution.importFromJson(r_file)

        print("\nSoluion test case:\n======================")
        print(self.solution)

    def test_json(self):
        pass
        #expectedJson = """[[2,0,1],[0,1,2],[1,2,0]]"""
        #actualJson = self.solution.exportToJson().replace(" ","").replace("\n","")

        #self.assertEqual(actualJson, expectedJson)

    def test_neighbourhood(self):
        print("\nNeighbourhood:")
        print(*self.solution.neighbourhood(), sep = "\n")
    def test_update_lines(self):
        newLines = [[0, 1, 2],[0, 1, 2],[0, 1, 2]]
        self.solution.updateLines(newLines)
        self.assertEqual(self.solution.lines, newLines)

if __name__== "__main__":
    unittest.main()