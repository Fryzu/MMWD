import settings
from math import inf
from City import City
from Solution import Solution
from Tabu_list import TabuList

class TaboAlgo:
    def __init__(self, city = None, solution = None, taboList = None, bestValue = None, bestNeighbourValue = None, neighbour = None):
        self.city = city
        #TaboAlgo can import city, taboList and solution from json
        if city:
            self.city = city
        else:
            self.city = City()
        if taboList:
            self.taboList = taboList
        else:
            self.taboList = TabuList()
        if solution:
            self.solution = solution
        else:
            self.solution = Solution()
        self.neighbour = Solution()##to ma byc nowa zmienna

    def iterate(self):
        n = 0
        self.solution.setCost(self.cost())
        best=Solution()
        best.setAll(self.solution)
        print(best)
        while n< settings.ITERATION:
            n += 1
            ##add solution to tabulist
            self.solution.setAll(self.nieghbourhood())
            if self.solution.getCost() < best.getCost():
                best.setAll(self.solution)
            self.taboList.add(self.solution)
            self.taboList.update()
            print(str(n)+'\n')
            self.taboList.print()
        return best

    def nieghbourhood(self):
        bestNieghbour = Solution()
        value = self.changeOneBusStop()
        if value.getCost() < bestNieghbour.getCost():
            bestNieghbour.setAll(value)
        return bestNieghbour
        pass

    def changeOneBusStop(self):## sąsiedztwo1: wymiana jednego przystanku z linii na inny jesli jest to możliwe
        bestsolution = Solution()
        for line in range(0,len(self.solution.lines)):
            for busStop in range(0, len(self.solution.lines[line])):
                if busStop == 0:
                    for x in range(0, settings.MAP_SIZE):
                        if self.city.getDistance(x,self.solution.lines[line][busStop+1]) != inf:
                            self.neighbour.updateLines(self.solution.getLines())##iezalezny obiekt
                            self.neighbour.updateBusStop(line,busStop,x)
                            if not self.taboList.check(self.neighbour):
                                self.neighbour.setCost(self.costNeighbour())
                                if self.neighbour.getCost() < bestsolution.getCost():
                                    bestsolution.setAll(self.neighbour)
                if busStop == len(self.solution.lines[line]) - 1:
                    for x in range(0, settings.MAP_SIZE):
                        if self.city.getDistance(self.solution.lines[line][busStop-1],x) != inf:
                            self.neighbour.updateLines(self.solution.getLines())##iezalezny obiekt
                            self.neighbour.updateBusStop(line,busStop,x)
                            if not self.taboList.check(self.neighbour):
                                self.neighbour.setCost(self.costNeighbour())
                                if self.neighbour.getCost() < bestsolution.getCost():
                                    bestsolution.setAll(self.neighbour)
                else:
                    for x in range(0, settings.MAP_SIZE):
                        if self.city.getDistance(self.solution.lines[line][busStop-1],x) != inf:
                            if self.city.getDistance(x,self.solution.lines[line][busStop+1]) != inf:
                                self.neighbour.updateLines(self.solution.getLines())##iezalezny obiekt
                                self.neighbour.updateBusStop(line,busStop,x)
                                if not self.taboList.check(self.neighbour):
                                    self.neighbour.setCost(self.costNeighbour())
                                    if self.neighbour.getCost() < bestsolution.getCost():
                                        bestsolution.setAll(self.neighbour)
        return bestsolution

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

    def costNeighbour(self):
        #Value function calculating
        result = 0
        #result = self.city.getTraffic(1, 2)
        for i in range(0, settings.MAP_SIZE):
            for j in range(0, settings.MAP_SIZE):
                if i != j:
                    result += self.checkNeighbour(i,j)*self.city.getTraffic(i, j)
        return result

    def checkNeighbour(self, x, y):
        minimum = 0
        globalmin = inf
        abd = 0
        for line in self.neighbour.lines: ##potem mozna robic do aktualniej liczby linii metoda do solution
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
