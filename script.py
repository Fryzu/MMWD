import settings
from Solution import Solution
from City import City
from TaboAlgo import TaboAlgo
import time
import os #files and directories
datasets_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "unitTests")
import matplotlib.pyplot as plt

settings.MAP_SIZE = 15
settings.LINE_LENGTH = 5
settings.LINES_NUMBER = 3
settings.ITERATION = 100
settings.TABUTIME = 20

print("Reading datasets... ", end='', flush=True)

city = City()
with open(os.path.join(datasets_dir, "test_city_15.json"), 'r') as r_file:
    city.importFromJson(r_file)
solution = Solution()

print("OK")
print("Initializing algorythm... ", end='', flush=True)

taboAlgo = TaboAlgo(city, solution)

print("OK")
print("Algo run... ", flush=True)
print("Start cost function value: ", "{:,}".format(taboAlgo.bestLinesCost))

print("|"," "*98, "|", flush=True)
costRun = []
costRun.append(taboAlgo.bestLinesCost)
i = 0
while i < settings.ITERATION:
    i=i+1
    taboAlgo.iterate()
    costRun.append(taboAlgo.actualCost)
    print("=", end='', flush=True)

plt.plot(range(settings.ITERATION+1), costRun)
plt.grid()
plt.show()
print("\nEnd cost function value: ", "{:,}".format(taboAlgo.bestLinesCost))

print("OK")
