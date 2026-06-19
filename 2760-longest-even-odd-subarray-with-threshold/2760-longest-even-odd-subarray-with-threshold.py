class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
         n = len(nums)
         res = 0
         i = 0
         while i < n:
             if nums[i] % 2 == 0 and nums[i] <= threshold:
                 j = i
                 while (j + 1 < n and nums[j + 1] <= threshold and nums[j] % 2 != nums[j + 1] % 2):
                     j += 1
                 res = max(res, j - i + 1)
                 i = j + 1
             else:
                 i += 1
         return res
        