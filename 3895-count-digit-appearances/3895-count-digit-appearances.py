class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        count=0
        for i in str(nums):
            if str(digit) in i:
                count+=1
        return count
        