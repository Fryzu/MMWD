from random import randint
from math import inf

MAX_DISTANCE = 50
MAX_TRAFFIC = 50
LINES_NUMBER = 3
LINE_LENGTH = 3
MAP_SIZE = 10
PENALITY_CONST = 1
FINE = 10000

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

    def getLine(self,i):
        return self.lines[i]

    @property
    def cost(self):##przekazanie referencji Solution?
        #Value function cresultalculating
        result = 0

        for i in range(0, MAP_SIZE):
            for j in range(0, MAP_SIZE):
                if i != j:
                    result += check(costam,i,j)*self.city.getTraffic(i, j)
        return result

    def check(self,x,y):
        busStopList =[]
        min = 0
        globalmin =0
        for i in range(0,LINES_NUMBER):##potem mozna robic do aktualniej liczby linii metoda do solution
            line = getLine(self,i)
            for j in range(0,line.len()):##przechodznie po lini w poszukiwaniu przystanku x
                if x == line[j]:## jesli znaleziono przystanek x
                    for m in range(0,line.len()):##szukanie przystanku Y w linii
                        if y == line[m]:
                            if x >y:
                                for n in range(x,y-1):
                                    min = min + self.getDistance(n,n+1)## wyznaczanie długosci trasy z x do y
                            else:
                                for n in range(y,x-1):
                                    min = min + self.getDistance(n,n+1)## to samo tylko dla przypadku y>x
                            if globalmin == 0 or globalmin >min:
                                globalmin = min##globalnie najmniejsza trasa
                            min = 0
                        else:
                            continue
                else:
                    continue
        if globalmin == 0:##jesli nigdzie nie znaleziono polączenia czyli globalmin  = 0 to wyslij kare
            return FINE
        else:
            return globalmin

    def __str__(self):
        result = '======SOLUTION======'
        for i in self.lines:
            result += '\n'
            result += str(i)
        return result  
