import settings
from math import inf
from City import City
from Solution import Solution
from Tabu_list import TabuList
import copy

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
        self.bestLines = copy.deepcopy(self.solution.getLines())
        self.bestLinesCost = self.cost()

    def iterate(self):
        neighbours = self.solution.neighbourhood() 
        for x in range(0, len(neighbours)):
            self.solution.updateLines(neighbours[x])
            actualCost = self.cost()
            if actualCost < self.bestLinesCost:
                self.bestLinesCost = actualCost
                self.bestLines = copy.deepcopy(self.solution.getLines())

        """ self.solution.setCost(self.cost())
        best = copy.deepcopy(self.neighbour)
        print(best)
        while n < iterationCount:
            n += 1
            ##add solution to tabulist
            self.solution = copy.deepcopy(self.nieghbourhood())
            if self.solution.getCost() < best.getCost():
                best.setAll(self.solution)
            self.taboList.add(self.solution)
            self.taboList.update()
            print(str(n)+'\n')
            self.taboList.print()
        return best """

    """ def nieghbourhood(self):
        bestNieghbour = Solution()
        value = self.changeOneBusStop()
        if value.getCost() < bestNieghbour.getCost():
            bestNieghbour.setAll(value)
        return bestNieghbour
        pass """
    
    def cost(self):
        #Value function calculating
        result = 0
        #result = self.city.getTraffic(1, 2)
        for i in range(0, settings.MAP_SIZE):
            for j in range(0, settings.MAP_SIZE):
                if i != j:
                    result += self.costFunctionCheck(i,j)*self.city.getTraffic(i, j)
        return result

    def costFunctionCheck(self, x, y):
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
