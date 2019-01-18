import settings
from Solution import Solution
from City import City
from TaboAlgo import TaboAlgo
import os
import matplotlib.pyplot as plt

datasets_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "datasets")

settings.MAP_SIZE = 15
settings.LINE_LENGTH = 5
settings.LINES_NUMBER = 10
settings.TABUTIME = 20

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()

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
stops = []
people = []

costRun.append(taboAlgo.bestLinesCost)
aspiration.append(taboAlgo.aspiration)
tabulen.append(taboAlgo.tabulen)
stops.append(100*taboAlgo.alanisybus())
people.append(100*taboAlgo.analisypeople())

while True:
    iterations_count = int(input("Insert iterarions count untill stop and summary: "))
    i = 0
    while i < iterations_count:
        taboAlgo.iterate()
        costRun.append(taboAlgo.actualCost)
        aspiration.append(taboAlgo.aspiration)
        tabulen.append(taboAlgo.tabulen)
        stops.append(100*taboAlgo.alanisybus())
        people.append(100*taboAlgo.analisypeople())
        printProgressBar(i+1, iterations_count, prefix = 'Progress:', suffix = 'Complete', length = 50)
        i=i+1

    f, axarr = plt.subplots(3, sharex=True)
    axarr[0].plot(range(len(costRun)), costRun)
    axarr[0].set_title('Cost function')
    axarr[1].plot(range(len(stops)), stops)
    axarr[1].set_title('Stops usage')
    axarr[2].plot(range(len(people)), people)
    axarr[2].set_title('People length')

    plt.grid()
    plt.show()

    f, axarr = plt.subplots(3, sharex=True)
    axarr[0].plot(range(len(costRun)), costRun)
    axarr[0].set_title('Cost function')
    axarr[1].plot(range(len(aspiration)), aspiration)
    axarr[1].set_title('Aspiration usage')
    axarr[2].plot(range(len(tabulen)), tabulen)
    axarr[2].set_title('Tabo length')

    plt.grid()
    plt.show()

    print("")
    print("Current solution: {}\ncost {}".format(taboAlgo.solution.lines, taboAlgo.actualCost))
    print("Current best solution: {}\ncost {}".format(taboAlgo.bestLines, taboAlgo.bestLinesCost))

    if not (input("Do you want to continue process? Y/n ") == "Y"):
        break

print("="*76)