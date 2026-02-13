from functools import lru_cache
class Solution:
    def findTargetSumWays(self, arr: List[int], target: int) -> int:
        @lru_cache(None)
        def backtrack(i, s):
            if i == len(arr):
                return 1 if s == target else 0
            
            return backtrack(i + 1, s + arr[i]) + backtrack(i + 1, s - arr[i])
        return backtrack(0, 0)
