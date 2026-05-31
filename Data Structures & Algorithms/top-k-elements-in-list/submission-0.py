class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqByNum = defaultdict(int)
        numsByFreq = defaultdict(set)

        for num in nums:
            freq = freqByNum[num]
            if num in numsByFreq[freq]:
                numsByFreq[freq].remove(num)
            newFreq = freq + 1
            freqByNum[num] = newFreq
            numsByFreq[newFreq].add(num)

        maxFreq = list(numsByFreq.keys())
        heapq._heapify_max(maxFreq)

        topKFreqNums = []
        while k > 0:
            freq = heapq._heappop_max(maxFreq)
            freqNums = numsByFreq[freq]
            for num in freqNums:
                if k <= 0:
                    return topKFreqNums
                topKFreqNums.append(num)
                k -= 1
        
        return topKFreqNums