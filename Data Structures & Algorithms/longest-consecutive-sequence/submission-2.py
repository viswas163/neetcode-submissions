class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        lenByNum = defaultdict(int)

        for num in nums:
            if lenByNum[num]:
                continue

            lenByNum[num] = lenByNum[num - 1] + lenByNum[num + 1] + 1
            lenByNum[num - lenByNum[num - 1]] = lenByNum[num]
            lenByNum[num + lenByNum[num + 1]] = lenByNum[num]
        
            longest = max(longest, lenByNum[num])
        
        return longest
