class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLen = 0

        for num in numSet:
            if (num - 1) not in numSet:
                streak = 1
                while (num + streak) in numSet:
                    streak += 1
                maxLen = max(maxLen, streak)
        return maxLen
