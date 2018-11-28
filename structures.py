from random import randint
from math import inf
from abc import ABC, abstractmethod

MAX_DISTANCE = 50
MAX_TRAFFIC = 50
LINES_NUMBER = 3
LINE_LENGTH = 3
MAP_SIZE = 3
PENALTY = 0

class Simulation:
    def simulate(self, iterationsCount, startPoint = None):
        '''Simulate iterationsCount iterations with starting point. 
        When no starting point generates random.'''
        pass

    def save():
        '''Ability to stop the simulation and save the status of solution and map'''
        pass

class ICity(ABC):
    '''City class interface for taboAlgo'''

    @abstractmethod
    def getDistance(self, firstNode: int, secondNode: int) -> int:
        pass

    @abstractmethod
    def getTraffic(self, firstNode: int, secondNode: int) -> int:
        pass

class ISolution(ABC):
    '''Solution class interface for taboAlgo'''

    @abstractmethod
    def neighbourhood(self) -> list:
        pass

    @abstractmethod
    def neighbourhood(self, lines: list):
        pass

class City(ICity):
    '''City map represents data of the problem'''

    def __init__(self):
        self._conncections = [[0 for x in range(MAP_SIZE)] for y in range(MAP_SIZE)] 
        for i in range(MAP_SIZE):
            for j in range(MAP_SIZE):
                if i != j:
                    randomDistance= randint(1, MAX_DISTANCE)
                    randomTraffic= randint(1, MAX_TRAFFIC)
                    newConncetion = {
                        "distance": randomDistance,
                        "traffic": randomTraffic
                    }
                    self._conncections[i][j] = newConncetion
                else:
                    newConncetion = {
                        "distance": inf,
                        "traffic": inf
                    }
                    self._conncections[i][j] = newConncetion
        for i in range(MAP_SIZE):
            for j in range(MAP_SIZE):
                if i >j:
                    self._conncections[i][j]["distance"] = self._conncections[j][i]["distance"]

    def getTraffic(self, firstNode, secondNode):
        return self._conncections[firstNode][secondNode]["traffic"]

    def getDistance(self, firstNode, secondNode):
        return self._conncections[firstNode][secondNode]["distance"]

    def __str__(self):
        result = 'CITY MAP\n================='
        for i in self._conncections:
            result += '\n'
            result += str(i)
        result += '\n'
        return result

    def printDistance(self):
        result = 'CITY MAP DISTANCE\n=================\n'
        for i in range(MAP_SIZE):
            for j in range(MAP_SIZE):
                connection = '{:>5}'.format(self._conncections[i][j]["distance"]) 
                result += connection
            result += "\n"
        return result

    def printTraffic(self):
        result = 'CITY MAP TRAFFIC\n=================\n'
        for i in range(MAP_SIZE):
            for j in range(MAP_SIZE):
                connection = '{:>5}'.format(self._conncections[i][j]["traffic"])
                result += connection
            result += "\n"
        return result

class Solution(ISolution):
    ''' Solution representation '''

    def __init__(self, city):

        self.city = city
        self.lines = []

        #generate list of lines
        for i in range(0, LINES_NUMBER):

            #generate random line
            line = []
            startStop = randint(0, MAP_SIZE-1)
            line.append(startStop)

            for i in range(1, LINE_LENGTH):
                nextStop = (line[i-1] + 1)%LINE_LENGTH
                line.append(nextStop)

            self.lines.append(line)

    @property
    def cost(self):##przekazanie referencji Solution?
        #Value function calculating
        result = 0
        #result = self.city.getTraffic(1, 2)
        for i in range(0, MAP_SIZE):
            for j in range(0, MAP_SIZE):
                if i != j:
                    result += self.check(i,j)*self.city.getTraffic(i, j)
        return result

    def check(self, x, y):
        minimum = 0
        globalmin = inf
        abd = 0
        for line in self.lines: ##potem mozna robic do aktualniej liczby linii metoda do solution
            for i in range(0, len(line)):##przechodznie po lini w poszukiwaniu przystanku x
                if line[i] == x:## jesli znaleziono przystanek x
                    for m in range(0, len(line)):##szukanie przystanku Y w linii
                        if line[m] == y:
                            minimum = 0
                            if m > i:
                                for n in range(i, m,1):
                                    minimum += self.city.getDistance(line[n], line[n+1])## to samo tylko dla przypadku y>x
                            if m < i:
                                for n in range(i, m,-1):
                                    minimum += self.city.getDistance(line[n], line[n-1])## to samo tylko dla przy
                            if globalmin > minimum:
                                globalmin = minimum##globalnie najmniejsza trasa
                        else:
                            continue
                else:
                    continue
        if globalmin == inf:##jesli nigdzie nie znaleziono polączenia czyli globalmin  = 0 to wyslij kare
            return PENALTY
        else:
            return globalmin

    def neighbourhood(self):
        pass

    def neighbourhood(self, lines):
        pass


    def __str__(self):
        result = '======SOLUTION======'
        for i in self.lines:
            result += '\n'
            result += "Line" + str(i)
        return result  
