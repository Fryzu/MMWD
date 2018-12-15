import unittest
from Solution import Solution
from City import City
import settings

class TabuList:
    def __init__(self):
        self.list = []


    def add(self, list):
        self.list.append([list,settings.TABUTIME])

    def update(self):
        for i in range(0,len(self.list)):
            self.list[i][1]-=1
        if self.list[0][1] == 0:
            self.list.pop(0)

    def check(self, List):
        if not self.list:
            return False
        for i in range(0,len(self.list)):
            if List == self.list[i][0]:
                return True
        return False

    def print(self):
        result = 'TABU\n======================'
        print(result)
        if list:
            for i in self.list:
                print('\n'+str(i[0])+'\n'+"TabuTIME: " + str(i[1]))
        return result