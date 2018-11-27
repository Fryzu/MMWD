### tabu search
from structures import *

ITERATION = 1000000

def tabooSearch():
    n = 0
    city = City()
    solution = Solution(city)
    while n < ITERATION:
        n = n + 1
