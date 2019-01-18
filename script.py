import settings
from Solution import Solution
from City import City
from TaboAlgo import TaboAlgo
import os
import matplotlib.pyplot as plt

datasets_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "datasets")

settings.MAP_SIZE = 15
settings.LINE_LENGTH = 5
settings.LINES_NUMBER = 3
settings.TABUTIME = 20

print("Tabu Search (TS) algorithm in a problem of public transport network creation")
print("@Sylwester Dawida, @Bartłomiej Fryz")
print("="*76)

# Initializing all the objects

while True:
    try:
        print("{}".format(os.listdir(datasets_dir)))
        dataset_name = input("Please enter dataset name from set above: ")
        city = City()
        with open(os.path.join(datasets_dir, dataset_name+".json"), 'r') as r_file:
            city.importFromJson(r_file)
        settings.MAP_SIZE = len(city._conncections)
        solution = Solution()
        print("ok")
        break
    except:    
        print('No such file as {}\n'.format(dataset_name), end='', flush=True)
taboAlgo = TaboAlgo(city, solution)
print("="*76)

# Iteration loop

costRun = []
aspiration = []
tabulen = []
costRun.append(taboAlgo.bestLinesCost)

while True:
    iterations_count = int(input("Insert iterarions count untill stop and summary: "))
    i = 0
    while i < iterations_count:
        taboAlgo.iterate()
        costRun.append(taboAlgo.actualCost)
        aspiration.append(taboAlgo.actualCost)
        tabulen.append(taboAlgo.actualCost)
        print("*", end='', flush=True)
        i=i+1
    plt.plot(range(len(costRun)), costRun)
    plt.grid()
    plt.show()

    print("")
    print("Current solution: {}\ncost {}".format(taboAlgo.solution.lines, taboAlgo.actualCost))
    print("Current best solution: {}\ncost {}".format(taboAlgo.bestLines, taboAlgo.bestLinesCost))

    if input("Do you want to end process? Y/n ") == "Y":
        break

print("="*76)
