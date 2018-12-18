import json

class Simulation:
    def __init__(self):
        #statuslist is a list that show how the solution parameters changed over process

    def simulate(self, iterationsCount):
        pass

    def saveStatus(self)
        pass

    def importFromJson(self, importPath):
        with open(importPath, 'r') as file_s:
            self.taboAlgo = json.load(file_s)

    def exportToJson(self, exportPath): 
        with open(importPath, 'w') as file_s:
            file_s.write(json.dumps(self.lines, indent=4, sort_keys=True))