import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # We can maybe have a loop of starting from the minimal k value and the first time it actually
        # Works we can then return it?
        # Now how would we go about going throguh the piles array for instance
        # [1,4,3,2] let's start with the first variable we'll keep it as 1
        # [1, 4, 3] already we have used 1, 4/1 = 4 (we'll have to use some divisor operator) and then 
        # It's 1 + 4 and then + 3 that's 
        
        left, right = 1, max(piles)
        while left < right: 
            middle = (left + right)//2
            current_time = 0
            for pile in piles:
                current_time += math.ceil(pile / middle)
            if current_time <= h:
                right = middle
            elif current_time > h: 
                left = middle + 1
        return left