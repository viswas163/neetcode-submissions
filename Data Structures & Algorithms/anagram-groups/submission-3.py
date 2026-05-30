from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groupsBySortedAnagram = defaultdict(list)

        for word in strs:
            charCounts = [0 for i in range(26)]
            for c in word:
                charIndex = ord(c) - 97
                charCounts[charIndex] += 1
            groupsBySortedAnagram[tuple(charCounts)].append(word)

        return list(groupsBySortedAnagram.values())
        