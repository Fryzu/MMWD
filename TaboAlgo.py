import settings
from math import inf

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

    def iterate(self):
        pass

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
            return settings.PENALTY
        else:
            return globalmin