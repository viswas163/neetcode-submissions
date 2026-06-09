class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        j = len(s) - 1
        
        while i <= j:
            while i < len(s) and not s[i].isalnum():
                i += 1
            while j >= 0 and not s[j].isalnum():
                j -= 1
            
            if i > j:
                break

            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True