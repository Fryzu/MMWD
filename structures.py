from random import randint
from math import inf

MAX_DISTANCE = 50
MAX_TRAFFIC = 50
LINES_NUMBER = 3
LINE_LENGTH = 3
MAP_SIZE = 3
PENALITY_CONST = 1

class City:
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

class Solution:
    ''' Solution representation '''

    def __init__(self, city):

        self.city = city
        self.lines = []

        #generate list of lines
        for i in range(0, LINES_NUMBER):
            lineName = "Line "+str(i)

            #generate random line
            line = []
            startStop = randint(0, MAP_SIZE-1)
            line.append(startStop)

            for i in range(1, LINE_LENGTH):
                nextStop = (line[i-1] + 1)%LINE_LENGTH
                line.append(nextStop)

            self.lines.append({
                lineName : line
            })

    @property
    def cost(self):
        #Value function cresultalculating
        result = 0

        for i in range(0, MAP_SIZE):
            for j in range(0, MAP_SIZE):
                if i != j:
                    result += 1*self.city.getTraffic(i, j)
        return result

    def __str__(self):
        result = '======SOLUTION======'
        for i in self.lines:
            result += '\n'
            result += str(i)
        return result  
