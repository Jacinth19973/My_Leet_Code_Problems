class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        left_close = 0
        left_far = 0
        odd_count = 0
        total_subarrays = 0
        for right in range(len(nums)):
            if nums[right] % 2 != 0:
                odd_count += 1                
            while odd_count > k:
                if nums[left_close] % 2 != 0:
                    odd_count -= 1
                left_close += 1
                left_far = left_close                 
            if odd_count == k:
                while nums[left_far] % 2 == 0:
                    left_far += 1                
                total_subarrays += (left_far - left_close) + 1
        return total_subarrays
