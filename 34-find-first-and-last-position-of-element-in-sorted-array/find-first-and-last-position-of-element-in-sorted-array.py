import numpy as np
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        last=r=first=-1
        n=len(nums)
        if n==0:
            return [-1,-1]
        for i in range(n):
            if nums[i]==target:
               if first == -1:
                    first = i
               last = i
            elif target not in nums:
                return [-1,-1]
        return [first,last]  
   