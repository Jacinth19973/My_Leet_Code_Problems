class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
            
        current = 1
        while current < n:
            current *= 3
            
        return current == n
