import unittest
from Solution import Solution

class TestSolution(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.solution = Solution()

        #imports test_file.json and loads it to the solution
        with open('C:/Users/Sylwester/PycharmProjects/MMWDd/tests/test_solution.json', 'r') as r_file:
            self.solution.importFromJson(r_file)

        print("\nSoluion test case:\n======================")
        print(self.solution)

    def test_json(self):
        expectedJson = """[[2,0,1],[0,1,2],[1,2,0]]"""
        actualJson = self.solution.exportToJson().replace(" ","").replace("\n","")

        self.assertEqual(actualJson, expectedJson)

    def test_neighbourhood(self):
        #TODO nieghbourhood
        pass

    def test_update_lines(self):
        newLines = [[0, 1, 2],[0, 1, 2],[0, 1, 2]]
        self.solution.updateLines(newLines)
        self.assertEqual(self.solution.lines, newLines)

if __name__== "__main__":
    unittest.main()
