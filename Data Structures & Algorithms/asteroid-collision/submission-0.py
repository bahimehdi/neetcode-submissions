# asteroids = array of int, relative point of each asteroid in space
# abs(asteroids[i]) = size of ith asteroid
# and its sign represents its direction (positive -> right, negative -> left) 'all move at the same speed'
# return: collisions:
# rules:
# 2 asteroids meet => the smaller one will explode => append the bigger and pop it
# if both are the same size, both will explode
# 2 asteroids moving in the same direction will never meet

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        i = 0
        while i < len(asteroids):
            survived = True
            if i < len(asteroids):
                while stack and (stack[-1] > 0 and asteroids[i] < 0):
                    if i == len(asteroids):
                        break
                    if abs(stack[-1]) == abs(asteroids[i]):
                        stack.pop()
                        survived = False
                        break
                    elif abs(stack[-1]) < abs(asteroids[i]):
                        stack.pop()
                        survived = True
                    else:
                        survived = False
                        break
                if survived:
                    stack.append(asteroids[i])
                i += 1
        return stack