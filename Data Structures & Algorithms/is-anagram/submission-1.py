class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letterMap = {}
        for c in s:
            if c not in letterMap:
                letterMap[c] = 0
            letterMap[c] = letterMap[c] + 1

        for c in t:
            if c not in letterMap:
                return False
            letterMap[c] = letterMap[c] - 1
            if letterMap[c] == 0:
                letterMap.pop(c)

        return len(letterMap) == 0
