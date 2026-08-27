# input:
# position = position of cars (in miles)
# speed = speed of cars (in miles/hour)
# Output:
# target = destination (in miles)
# = number of different car fleets that will arrive at the destination
# Rules:
# A car cannot pass another car ahead of it
# but, can catch up to another car and then drive at the same speed as the car ahead of it
# Car fleet = non-e,pty set of cars driving at (same position, same speed) 'a single car could be considered as a car fleet'
# If a car catches up to a car fleet, the moment the fleet reaches the destination, then the car is considered to be part of the fleet

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = list(zip(position, speed))
        fleets.sort()
        destination, i = 1, len(fleets) - 1
        iterationsNecessaryNext = (target - fleets[-1][0]) / fleets[-1][1]
        while i >= 1:
            iterationsNecessary = iterationsNecessaryNext
            iterationsNecessaryNext = (target - fleets[-2][0]) / fleets[-2][1]
            if iterationsNecessary >= iterationsNecessaryNext:
                fleets.pop(-2)
                iterationsNecessaryNext = iterationsNecessary
            else:
                fleets.pop()
                destination += 1
            i -= 1
        return destination






# [1, 4] [3,2] 'while target < max(position)
# iter1: [(4, 3), (6, 2)]
# iter2: [(7, 3), (8, 2)]
# iter3: [(10, 3), (10, 2)] => [(10,2)] one fleet (we return then len(fleets))