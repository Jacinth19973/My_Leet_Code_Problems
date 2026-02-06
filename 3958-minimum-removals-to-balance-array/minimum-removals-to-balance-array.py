class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort() 
        left=0
        for right in range(len(nums)):
            if nums[right] > nums[left]*k:
                left+=1
        return left