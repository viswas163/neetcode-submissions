class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        self.groups = []
        self.groupIndexBySortedAnagram = {}

        for word in strs:
            sortedWord = "".join(sorted(word))
            if sortedWord in self.groupIndexBySortedAnagram:
                groupIndex = self.groupIndexBySortedAnagram.get(sortedWord)
                self.groups[groupIndex].append(word)
            else:
                self.groupIndexBySortedAnagram[sortedWord] = len(self.groups)
                self.groups.append([word])

        return self.groups
        