import settings
from math import inf
from City import City
from Solution import Solution

class TaboAlgo:
    def __init__(self, city = None, solution = None, taboList = None):
        self.city = city
        #TaboAlgo can import city, taboList and solution from json
        if city:
            self.city = city
        else:
            self.city = City()
        if taboList:
            self.taboList = taboList
        else:
            self.taboList = []
        if solution:
            self.solution = solution
        else:
            self.solution = Solution()
        self.bestValue = self.cost()
        self.bestNieghbourValue = inf

    def iterate(self):
        n = 0
        while n< settings.ITERATION:
            n += 1
            ##add solution to tabulist
            self.solution = self.nieghbourhood()
            Cost = self.cost()
            if Cost < self.bestValue:
                self.bestValue = Cost
        return self.solution

    def nieghbourhood(self):
        lines = self.solution.lines
        self.bestNieghbourValue = inf
        value = changeOneBusStop()
        if value < self.bestNieghbourValue
            self.bestNieghbourValue = value
        pass

    def changeOneBusStop(self):## sąsiedztwo1: wymiana jednego przystanku z linii na inny jesli jest to możliwe
        globalValue = inf
        bestsolution = 0
        backup = self.solution.lines
        lines = self.solution.lines
        for line in range(0,len(lines)):
            for busStop in range(0, len(line)):
                if busStop == 0:
                    for x in range(0, settings.MAP_SIZE):
                        if self.city.getDistance(x,lines[line][busStop+1]) != inf:
                            lines[line][busStop] = x
                            self.solution.lines = lines
                            Cost = self.cost()
                            if Cost < globalValue:
                                globalValue = Cost
                                bestsolution = lines
                if busStop == len(line) - 1:
                    for x in range(0, settings.MAP_SIZE):
                        if self.city.getDistance(line[busStop-1],x) != inf:
                            lines[line][busStop] = x
                            self.solution.lines = lines
                            Cost = self.cost()
                            if Cost < globalValue:
                                globalValue = Cost
                                bestsolution = lines
                else:
                    for x in range(0, settings.MAP_SIZE):
                        if self.city.getDistance(line[busStop-1],x) != inf:
                            if self.city.getDistance(x,line[busStop+1]) != inf:
                                lines[line][busStop] = x
                                self.solution.lines = lines
                                Cost = self.cost()
                                if Cost < globalValue:
                                    globalValue = Cost
                                    bestsolution = lines
        return bestsolution

    @property
    def cost(self):
        #Value function calculating
        result = 0
        #result = self.city.getTraffic(1, 2)
        for i in range(0, settings.MAP_SIZE):
            for j in range(0, settings.MAP_SIZE):
                if i != j:
                    result += self.check(i,j)*self.city.getTraffic(i, j)
        return result

    def check(self, x, y):
        minimum = 0
        globalmin = inf
        abd = 0
        for line in self.solution.lines: ##potem mozna robic do aktualniej liczby linii metoda do solution
            for i in range(0, len(line)):##przechodznie po lini w poszukiwaniu przystanku x
                if line[i] == x:## jesli znaleziono przystanek x
                    for m in range(0, len(line)):##szukanie przystanku Y w linii
                        if line[m] == y:
                            minimum = 0
                            if m > i:
                                for n in range(i, m,1):
                                    next = self.city.getDistance(line[n], line[n+1])
                                    if next == inf:## zabezpieczenie przed inf czyli braku połączenia między przystankami
                                        minimum = inf
                                        break
                                    minimum += next## to samo tylko dla przypadku y>x
                            if m < i:
                                for n in range(i, m,-1):
                                    next = self.city.getDistance(line[n], line[n-1])
                                    if next == inf:
                                        minimum = inf
                                        break
                                    minimum += next## to samo tylko dla przy
                            if globalmin > minimum:
                                globalmin = minimum##globalnie najmniejsza trasa
                        else:
                            continue
                else:
                    continue
        if globalmin == inf:##jesli nigdzie nie znaleziono polączenia czyli globalmin  = 0 to wyslij kare
            return settings.PENALTY
        else:
            return globalmin

