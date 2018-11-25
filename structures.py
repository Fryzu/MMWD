from random import randint

MAX_DISTANCE = 50
MAX_TRAFFIC = 50
LINES_NUMBER = 3
LINE_LENGTH = 3
MAP_SIZE = 3

class AlgoInterface:
    '''Interface for taboo search algorythm'''
    pass

class City(AlgoInterface):
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
    def __str__(self):
        result = '======CITY MAP======'
        for i in self._conncections:
            result += '\n'
            result += str(i)
        return result

    def printDistance(self):
        result = '======CITY MAP DISTANCE======\n'
        for i in range(MAP_SIZE):
            for j in range(MAP_SIZE):
                result += str(self._conncections[i][j].get("distance")) + "   "
            result += "\n"
        print(result)

class Solution:
    ''' Solution representation '''

    def __init__(self):
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

    def __str__(self):
        result = '======SOLUTION======'
        for i in self.lines:
            result += '\n'
            result += str(i)
        return result  

'''
    def __init__(self):
        self._lines = []

    def addLine(self, line = None):
        if line == None:
            line = Line()
        self._lines.append(line)

    def addConnection(self, lineNumber, connection):
        for i in self._lines:
            if i.number == lineNumber:
                i.addConncection(connection)

    def __str__(self):
        result = '======SOLUTION======'
        for i in self._lines:
            result += '\n\t'
            result += str(i)
        return result '''
