from collections import Counter
class Solution:
    def intersection(self,nums: list[list[int]]) -> list[int]:
        total_arrays = len(nums)
        counts = Counter(num for sub_list in nums for num in sub_list)
        return [x for x in range(1, 1001) if counts[x] == total_arrays]

    
