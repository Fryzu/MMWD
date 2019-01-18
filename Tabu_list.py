import unittest
from Solution import Solution
from City import City
import settings

class TabuList:
    def __init__(self):
        self.list = []

    def add(self, list):
        """if list["type"] == "move":
            self.list.append({"type":list["type"],
                              "line":list["line"],
                              "busStop": list["busStop"],
                              "remove":list["add"],
                              "add":list["remove"],
                              "tabutime":settings.TABUTIME})"""
        if list["type"] == "move":
            self.list.append({"type":list["type"],
                               "line":list["line"],
                              "first":list["remove"],
                              "second":list["add"],
                              "tabutime":settings.TABUTIME})
        if list["type"] == "swap":
            self.list.append({"type":list["type"],
                              "line":list["line"],
                              "busStopA":list["busStopA"],
                              "busStopB":list["busStopB"],
                              "first":list["first"],
                              "second":list["second"],
                              "tabutime":settings.TABUTIME})


    def update(self):
        for i in range(0,len(self.list)):
            self.list[i]["tabutime"]-=1
        if self.list[0]["tabutime"] == 0:
            self.list.pop(0)

    def check(self, List):
        if not self.list:
            return False
        """for i in range(0,len(self.list)):
            if List["type"] == self.list[i]["type"] and List["line"] == self.list[i]["line"] and \
            List["busStop"] == self.list[i]["busStop"] and List["remove"] == self.list[i]["remove"] and List["add"] == self.list[i]["add"]:
                return True"""
        for i in range(0,len(self.list)):
            if List["type"] == "move" and self.list[i]["type"] == "move":
                if List["line"] == self.list[i]["line"] and \
                    ((List['add'] == self.list[i]['first'] and List["remove"] == self.list[i]["second"])or
                    (List['add'] == self.list[i]['second'] and List["remove"] == self.list[i]["first"])):
                    return True
            if List["type"] == "swap" and self.list[i]["type"] == "swap":
                if List["line"] == self.list[i]["line"] and \
                        ((List['first'] == self.list[i]['first'] and List["second"] == self.list[i]["second"])or
                         (List['first'] == self.list[i]['second'] and List["second"] == self.list[i]["first"])):
                    return True
            else:
                continue
        return False

    def print(self):
        result = 'TABU\n======================'
        print(result)
        if list:
            for i in self.list:
                pass#print('\n'+str(i[0])+str(i[1])+'\n'+"TabuTIME: " + str(i[2]))
        return result

    def len(self):
        return len(self.list)
