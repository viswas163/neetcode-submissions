class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqNums = [[] for i in range(len(nums) + 1)]
        numsByFreq = defaultdict(set)
        freqByNum = defaultdict(int)

        for num in nums:
            prevFreq = freqByNum[num]
            if num in numsByFreq[prevFreq]:
                numsByFreq[prevFreq].remove(num)
            newFreq = prevFreq + 1
            freqByNum[num] = newFreq
            numsByFreq[newFreq].add(num)

        for freq, fNums in numsByFreq.items():
            freqNums[freq] = list(fNums)

        topKFreqNums = []
        for freq in range(len(freqNums) - 1, -1, -1):
            for freqNum in freqNums[freq]:
                topKFreqNums.append(freqNum)
                if len(topKFreqNums) == k:
                    return topKFreqNums
                
        return topKFreqNums