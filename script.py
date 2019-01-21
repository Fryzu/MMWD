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
        print("{} or random".format(os.listdir(datasets_dir)))
        dataset_name = input("Please enter dataset name from set above: ")
        if dataset_name == "random":
            dataset_size = input("Please enter city size: ")
            settings.MAP_SIZE = int(dataset_size)
            city = City()
            print(dataset_size)
        else:
            city = City()
            with open(os.path.join(datasets_dir, dataset_name+".json"), 'r') as r_file:
                city.importFromJson(r_file)
            settings.MAP_SIZE = len(city._conncections)
        print("ok")
        break
    except:    
        print('No such file as {}\n'.format(dataset_name), end='', flush=True)

print("="*76)
tmp = input("Please enter number of lines: ")
settings.LINES_NUMBER = int(tmp)
tmp = input("Please enter length of lines: ")
settings.LINE_LENGTH= int(tmp)
tmp = input("Please enter tabo time: ")
settings.TABUTIME= int(tmp)
solution = Solution()
print("ok")

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
    print("before: {}\ncost {}".format(taboAlgo.solution.lines, taboAlgo.actualCost))
    while i < iterations_count:
        taboAlgo.iterate()
        costRun.append(taboAlgo.actualCost)
        aspiration.append(taboAlgo.aspiration)
        tabulen.append(taboAlgo.tabulen)
        stops.append(100*taboAlgo.alanisybus())
        people.append(100*taboAlgo.analisypeople())
        printProgressBar(i+1, iterations_count, prefix = 'Progress:', suffix = 'Complete', length = 50)
        i=i+1

    plt.subplot(3, 2, 1)
    plt.plot(range(len(costRun)), costRun)
    plt.xlabel('Iteracja i')
    plt.ylabel('V(i)')
    plt.title('Funkcja celu')
    plt.grid(True)

    plt.subplot(3, 2, 2)
    plt.plot(range(len(stops)), stops)
    plt.title('Procentowa obsługa przystanków')
    plt.xlabel('Iteracja i')
    plt.ylabel('Ilość przystanków [%]')
    plt.grid(True)

    plt.subplot(3, 2, 3)
    plt.plot(range(len(people)), people)
    plt.title('Procentowa obsługa ludzi')
    plt.xlabel('Iteracja i')
    plt.ylabel('Ilość osób [%]')
    plt.grid(True)

    plt.subplot(3, 2, 4)
    plt.plot(range(len(aspiration)), aspiration)
    plt.title('Ilość wywołań kryterium aspiracji')
    plt.xlabel('Iteracja i')
    plt.ylabel('Wywołania')
    plt.grid(True)

    plt.subplot(3, 2, 5)
    plt.plot(range(len(tabulen)), tabulen)
    plt.title('Długość tablicy tabu')
    plt.xlabel('Iteracja i')
    plt.ylabel('Długość')
    plt.grid(True)

    plt.subplot(3, 2, 6)
    plt.plot(range(len(taboAlgo.index)), taboAlgo.index)
    plt.title('Powtarzające się rozwiązania')
    plt.xlabel('Iteracja i')
    plt.ylabel('Długość')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

    print("")
    print("Current solution: {}\ncost {}".format(taboAlgo.solution.lines, taboAlgo.actualCost))
    print("Current best solution: {}\ncost {}".format(taboAlgo.bestLines, taboAlgo.bestLinesCost))

    if not (input("Do you want to continue process? Y/n ") == "Y"):
        break

print("="*76)