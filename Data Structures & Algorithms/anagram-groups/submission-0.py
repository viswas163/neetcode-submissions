class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        for word in strs:
            groupIndex = self.getAnagramGroupIndex(word, groups)
            if groupIndex == None:
                groups.append([word])
            else:
                groups[groupIndex].append(word)
        return groups
    
    def getAnagramGroupIndex(self, word: str, groups: List[List[str]]) -> int | None:
        for i, group in enumerate(groups):
            if self.isAnagram(word, group[0]):
                return i
        return None
        
    def isAnagram(self, a: str, b: str) -> bool:
        if len(a) != len(b):
            return False
        return sorted(a) == sorted(b)
        