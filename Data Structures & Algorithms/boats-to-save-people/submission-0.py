# list of people, people[i] = weight of person i
# a boat can 1-2 people, a boat can carry up to limit in weight
# return min(boats) where every person is carried
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l, r = 0, len(people) - 1
        boats = 0
        people = sorted(people)
        while l < r:
            while (people[l] + people[r] > limit) and l <= r:
                boats += 1
                r -= 1
            while (people[l] + people[r] == limit) and l < r:
                boats += 1
                l += 1
                r -= 1
            if people[l] + people[r] < limit:
                boats += 1
                l += 1
                r -= 1
        if l == r:
            boats += 1

        return boats