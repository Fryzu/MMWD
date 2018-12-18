import unittest
import settings
from Solution import Solution
import os

project_dir = os.path.dirname(os.path.abspath(__file__))

class TestSolution(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        settings.MAP_SIZE = 15
        settings.LINE_LENGTH = 5
        settings.LINES_NUMBER = 3