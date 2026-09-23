class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for each in asteroids:
            alive = True
            
            while(alive and stack and stack[-1] > 0 and each < 0):
                top = stack[-1]
                if top < abs(each):
                    stack.pop()
                elif top == abs(each):
                    stack.pop()
                    alive = False
                else:
                    alive = False
            if alive:
                stack.append(each)
        return stack