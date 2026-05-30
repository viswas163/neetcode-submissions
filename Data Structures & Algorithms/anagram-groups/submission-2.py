class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groupsBySortedAnagram = defaultdict(list)

        for word in strs:
            sortedWord = "".join(sorted(word))
            groupsBySortedAnagram[sortedWord].append(word)

        return list(groupsBySortedAnagram.values())
        