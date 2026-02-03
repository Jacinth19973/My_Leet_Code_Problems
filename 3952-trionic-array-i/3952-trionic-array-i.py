class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 4:
            return False    
        p = 0
        while p + 1 < n and nums[p] < nums[p + 1]:
            p += 1
         
        if p == 0:
            return False
            
        q = p
        while q + 1 < n and nums[q] > nums[q + 1]:
            q += 1
           
        if q == p or q == n - 1:
            return False
            
        i = q
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
      
        return i == n - 1
