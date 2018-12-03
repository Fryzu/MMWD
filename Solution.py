from random import randint
from math import inf
from abc import ABC, abstractmethod
import json
import settings


class ISolution(ABC):
    '''Solution class interface for taboAlgo'''

    @abstractmethod
    def neighbourhood(self) -> list:
        pass

    @abstractmethod
    def updateLines(self, lines: list):
        pass

class Solution(ISolution):
    cost = inf
    ''' Solution representation '''

    def __init__(self):

        self.lines = []
        #generate list of lines
        for i in range(0, settings.LINES_NUMBER):

            #generate random line
            line = []

            startStop = randint(0, settings.MAP_SIZE-1)
            line.append(startStop)

            for i in range(1, settings.LINE_LENGTH):
                nextStop = (line[i-1] + 1)%settings.LINE_LENGTH
                line.append(nextStop)

            self.lines.append(line)

    def updateLines(self, lines):
        self.lines = lines

    def updateBusStop(self,i,j,value):
        self.lines[i][j] = value

    def getLines(self):
        return self.lines.copy()

    def getCost(self):
        return self.cost

    def setCost(self,cost):
        self.cost = cost

    def setAll(self,solution):
        self.lines = solution.getLines()
        self.cost = solution.getCost()

    def isequal(self,solution):
        if self.lines == solution.lines:
            return True
        else:
            return False

    def neighbourhood(self):
        pass

    def importFromJson(self, jsonString):
        self.lines = json.load(jsonString)

    def exportToJson(self):
        return json.dumps(self.lines, indent=4, sort_keys=True)

    def __str__(self):
        result = 'SOLUTION\n======================'
        for i in self.lines:
            result += '\n'
            result += "Line" + str(i)
        result += '\n'+"Cost: " + str(self.cost)
        return result
