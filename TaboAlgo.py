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
        self.bestLinesCost = self.cost(self.solution.lines)

    def iterate(self):
        neighbours = self.solution.neighbourhood()
        best = self.findBest(neighbours)
        if(best == False):
            print("pusta lista tabu")
            return False
        self.solution.lines = copy.deepcopy(best)
        actualCost = self.cost(self.solution.lines)
        if actualCost < self.bestLinesCost:
            self.bestLinesCost = actualCost
            self.bestLines = copy.deepcopy(self.solution.lines)
        self.taboList.add(copy.deepcopy(self.solution.lines))
        self.taboList.update()


        """for x in range(0, len(neighbours)):
            if not self.taboList.check(neighbours[x]):
                self.solution.updateLines(neighbours[x])
                actualCost = self.cost()
                if x == 0:
                    bestNeighbourCost = actualCost
                    bestNeighbour = copy.deepcopy(self.solution.getLines())
                if actualCost < bestNeighbourCost:
                    bestNeighbourCost = actualCost
                    bestNeighbour = copy.deepcopy(self.solution.getLines())
        if bestNeighbourCost < self.bestLinesCost:
            self.bestLinesCost = bestNeighbourCost
            self.bestLines = copy.deepcopy(bestNeighbour)
        self.solution.updateLines(copy.deepcopy(bestNeighbour))
        self.taboList.add(bestNeighbour)
        self.taboList.update()"""

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
    
    def cost(self,lines = None):
        if lines == None:
            lines = self.solution.lines
        #Value function calculating
        result = 0
        #result = self.city.getTraffic(1, 2)
        for i in range(0, settings.MAP_SIZE):
            for j in range(0, settings.MAP_SIZE):
                if i != j:
                    result += self.costFunctionCheck(i,j,lines)*self.city.getTraffic(i, j)
        return result

    def costFunctionCheck(self, x, y, lines):
        minimum = 0
        globalmin = inf
        abd = 0
        for line in lines: ##potem mozna robic do aktualniej liczby linii metoda do solution
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

    def findBest(self,neighbours):
        if not neighbours:##is not empty
            return False
        neighbours = self.filtr(neighbours)
        actualcost = self.cost(self.solution.lines)
        best = actualcost -  self.cost(neighbours[0])
        bestneighbour = neighbours[0]
        for neighbour in neighbours:
            if not self.taboList.check(neighbour):##is in tabu list ?
                cost = actualcost - self.cost(neighbour)
                if(cost>best):
                    best = cost
                    bestneighbour = neighbour
        return bestneighbour

    def filtr(self,neighbours):
    ##sprawdz czy jest polaczenie miedzy przystankami
        #toRemove = []
        for i in range(0,len(neighbours)):
            count = neighbours.count(neighbours[i])
            if count>1:
                for n in range(0,count-1):
                    index = neighbours.index((neighbours[i]))
                    #toRemove.append(index)
                    neighbours[index] = False
        neighbours = [elem for elem in neighbours if elem != False]#usuwanie elementów z false
        #toRemove.clear()##usuwanie powtarzajacych sie elementow etap pierwszy usuwanie powtarzających się linii w liscie neighbours
        """for solution in range(0,len(neighbours)):
            flag = 0
            if neighbours[solution] != False:
                for line in range(0,len(neighbours[solution])):
                    if flag == 1:
                        break
                    for busa in range(0,len(neighbours[solution][line])):
                        count = neighbours[solution][line].count(neighbours[solution][line][busa])
                        if count>1:
                            flag = 1
                            break
            if flag == 1:
                neighbours[i] = False
            neighbours = [elem for elem in neighbours if elem != False]#usuwanie elementów z false
            #toRemove.clear()##etap 2 usuwanie linii w których przystanki powtarzają sie
        """
        return neighbours

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


