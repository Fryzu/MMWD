from random import randint
from math import inf
from abc import ABC, abstractmethod
import json
import settings
import copy

class ISolution(ABC):
    '''Solution class interface for taboAlgo'''

    @abstractmethod
    def neighbourhood(self) -> list:
        pass

    @abstractmethod
    def updateLines(self, lines: list):
        pass

class Solution(ISolution):
    ''' Solution representation '''

    def __init__(self, lines = None):
        if lines:
            self.lines = lines
        else:
            self.lines = []
            #generate list of lines
            for m in range(0, settings.LINES_NUMBER):

                #generate random line
                gen = []
                for i in range(0, settings.MAP_SIZE):
                    gen.append(i)

                line = []

                for j in range(0, settings.LINE_LENGTH):
                    nextStop = randint(0, len(gen)-1)
                    line.append(gen[nextStop])
                    gen.remove(gen[nextStop])

                self.lines.append(line)

    def importFromJson(self, jsonString):
        self.lines = json.load(jsonString)

    def exportToJson(self):
        return json.dumps(self.lines, indent=4, sort_keys=True)

    def __str__(self):
        result = 'SOLUTION\n======================'
        for i in self.lines:
            result += '\n'
            result += "Line" + str(i)
        return result

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

    def isequal(self, solution):
        if self.lines == solution.lines:
            return True
        else:
            return False

    def neighbourhood(self):
        neigbourhood = []
        neigbourhood += self.changeOneBusStop()# change 1 busstop if it is possible
        neigbourhood += self.swapBusStop()#swap 2 in one line

        return neigbourhood

    def swapBusStop(self):
        swap = []
        swap.clear()
        # TODO: sprawdzic czy nie ma 2 identycznych przystankow

        for line in range(0, len(self.lines)):
            # for one line
            for busStop in range(0, len(self.lines[line])):
                for busStopB in range (0 ,len(self.lines[line])):
                    if busStop != busStopB:
                        swap.append({"type":"swap",
                                     "line":line,
                                     "busStopA": busStop,
                                     "busStopB": busStopB,
                                     "first":self.lines[line][busStop],
                                     "second":self.lines[line][busStopB]})
                        if swap.count({"type":"swap",
                                       "line":line,
                                       "busStopA": busStopB,
                                       "busStopB": busStop,
                                       "first":self.lines[line][busStopB],
                                       "second":self.lines[line][busStop]}):
                                swap.pop()
        return swap
        pass
    # types of neighbourhoods
    def changeOneBusStop(self):## sąsiedztwo1: wymiana jednego przystanku z linii na inny jesli jest to możliwe

        move = []
        move.clear()
        # TODO: sprawdzic czy nie ma 2 identycznych przystankow

        for line in range(0, len(self.lines)):
            # for one line
            for busStop in range(0, len(self.lines[line])):
                if busStop == 0:
                    for x in range(0, settings.MAP_SIZE):
                        # check if connection exists
                        if x != self.lines[line][busStop+1]and x != self.lines[line][busStop] and not self.isAlredyInLine(x,line):
                            move.append({"type":"move",
                                         "line":line,
                                         "busStop": busStop,
                                         "remove":self.lines[line][busStop],
                                         "add":x})
                            if move.count(move[-1]) > 1:
                                move.pop()
                if busStop == len(self.lines[line]) - 1:
                    for x in range(0, settings.MAP_SIZE):
                        if x != self.lines[line][busStop-1]and x != self.lines[line][busStop]and not self.isAlredyInLine(x,line):
                            move.append({"type":"move",
                                         "line":line,
                                         "busStop": busStop,
                                         "remove":self.lines[line][busStop],
                                         "add":x})
                            if move.count(move[-1]) > 1:
                                move.pop()
                else:
                    for x in range(0, settings.MAP_SIZE):
                        if x != self.lines[line][busStop+1] and x != self.lines[line][busStop-1] and x != self.lines[line][busStop] and not self.isAlredyInLine(x,line):
                            move.append({"type":"move",
                                         "line":line,
                                         "busStop": busStop,
                                         "remove":self.lines[line][busStop],
                                         "add":x})
                            if move.count(move[-1]) > 1:
                                move.pop()
        return move

    def isAlredyInLine(self,x,line):
        for i in range(0, len(self.lines[line])):
            if x == self.lines[line][i]:
                return True
        return False
