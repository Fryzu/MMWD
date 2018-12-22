import unittest
from Solution import Solution
from City import City
import settings

class TabuList:
    def __init__(self):
        self.list = []

    def add(self, list):
        if list["type"] == "move":
            self.list.append({"type":list["type"],
                              "line":list["line"],
                              "busStop": list["busStop"],
                              "remove":list["add"],
                              "add":list["remove"],
                              "tabutime":settings.TABUTIME})
        #if list[0] == "move":
           # self.list.append(["add",list[3],settings.TABUTIME])
            #self.list.append(["remove",list[4],settings.TABUTIME])


    def update(self):
        for i in range(0,len(self.list)):
            self.list[i]["tabutime"]-=1
        if self.list[0]["tabutime"] == 0:
            self.list.pop(0)

    def check(self, List):
        if not self.list:
            return False
        for i in range(0,len(self.list)):
            if List["type"] == self.list[i]["type"] and List["line"] == self.list[i]["line"] and \
            List["busStop"] == self.list[i]["busStop"] and List["remove"] == self.list[i]["remove"] and List["add"] == self.list[i]["add"]:
                return True
        return False

    def print(self):
        result = 'TABU\n======================'
        print(result)
        if list:
            for i in self.list:
                print('\n'+str(i[0])+str(i[1])+'\n'+"TabuTIME: " + str(i[2]))
        return result