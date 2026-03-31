class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        write = 1
        prev = nums[0]

        for i in range(1, n):
            curr = nums[i]
            if curr != prev:
                nums[write] = curr
                write += 1
                prev = curr

        return write
