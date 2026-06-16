class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        less = sum(num < target for num in nums)
        equal = sum(num == target for num in nums)
        return list(range(less, less + equal))
