from random import randint
from math import inf
from abc import ABC, abstractmethod
import json
import settings

class ICity(ABC):
    '''City class interface for taboAlgo'''

    @abstractmethod
    def getDistance(self, firstNode: int, secondNode: int) -> int:
        pass

    @abstractmethod
    def getTraffic(self, firstNode: int, secondNode: int) -> int:
        pass

class City(ICity):
    '''City map represents data of the problem'''

    def __init__(self):
        '''Generates random city when called, then we can change it by importFromJson'''

        self._conncections = [[0 for x in range(settings.MAP_SIZE)] for y in range(settings.MAP_SIZE)] 
        for i in range(settings.MAP_SIZE):
            for j in range(settings.MAP_SIZE):
                if i != j:
                    randomDistance= randint(1, settings.MAX_DISTANCE)
                    randomTraffic= randint(1, settings.MAX_TRAFFIC)
                    newConncetion = {
                        "distance": randomDistance,
                        "traffic": randomTraffic
                    }
                    self._conncections[i][j] = newConncetion
                else:
                    newConncetion = {
                        "distance": inf,
                        "traffic": inf
                    }
                    self._conncections[i][j] = newConncetion
        for i in range(settings.MAP_SIZE):
            for j in range(settings.MAP_SIZE):
                if i >j:
                    self._conncections[i][j]["distance"] = self._conncections[j][i]["distance"]

    def getTraffic(self, firstNode, secondNode):
        return self._conncections[firstNode][secondNode]["traffic"]

    def getDistance(self, firstNode, secondNode):
        return self._conncections[firstNode][secondNode]["distance"]

    def exportToJson(self):
        return json.dumps(self._conncections, indent=4, sort_keys=True)

    def importFromJson(self, jsonString):
        self._conncections = json.load(jsonString)

    def __str__(self):
        result = 'CITY MAP\n================='
        for i in self._conncections:
            result += '\n'
            result += str(i)
        result += '\n'
        return result

    def printDistance(self):
        result = 'CITY MAP DISTANCE\n======================\n'
        result += '{:>5}'.format("S1\S2")
        for j in range(settings.MAP_SIZE):
            result += '{:>5}'.format(j)
        result += "\n"

        for i in range(settings.MAP_SIZE):
            result += '{:>5}'.format(i)
            for j in range(settings.MAP_SIZE):
                connection = '{:>5}'.format(self._conncections[i][j]["distance"]) 
                result += connection
            result += "\n"
        return result

    def printTraffic(self):
        result = 'CITY MAP TRAFFIC\n======================\n'

        result += '{:>5}'.format("S1\S2")
        for j in range(settings.MAP_SIZE):
            result += '{:>5}'.format(j)
        result += "\n"

        for i in range(settings.MAP_SIZE):
            result += '{:>5}'.format(i)
            for j in range(settings.MAP_SIZE):
                connection = '{:>5}'.format(self._conncections[i][j]["traffic"])
                result += connection
            result += "\n"
        return result