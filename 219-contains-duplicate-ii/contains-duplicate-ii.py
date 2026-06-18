class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen_map = {}        
        for i, num in enumerate(nums):
            if num in seen_map and i - seen_map[num] <= k:
                return True            
            seen_map[num] = i
        return False
