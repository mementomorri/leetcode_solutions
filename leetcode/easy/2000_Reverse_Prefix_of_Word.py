class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        target = word.find(ch) +1
        left, right = word[:target], word[target:]
        result = left[::-1] + right
        return result
