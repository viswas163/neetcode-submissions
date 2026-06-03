class Solution:
    def encode(self, strs: List[str]) -> str:
        charDelim = ","
        wordDelim = "&"
        wordPrefix = "$"
        encodedWords = []

        if len(strs) == 0:
            return ""

        for word in strs:
            encodedChars = [str(ord(char)) for char in word]
            encodedWords.append(f"{wordPrefix}{charDelim.join(encodedChars)}")

        return wordDelim.join(encodedWords)

    def decode(self, s: str) -> List[str]:
        charDelim = ","
        wordDelim = "&"
        decodedWords = []

        if len(s) == 0:
            return []

        for word in s.split(wordDelim):
            encodedChars = word[1:].split(charDelim)
            if "".join(encodedChars) == "":
                decodedChars = ""
            else:
                decodedChars = [chr(int(char)) for char in encodedChars]
            decodedWords.append("".join(decodedChars))

        return decodedWords
