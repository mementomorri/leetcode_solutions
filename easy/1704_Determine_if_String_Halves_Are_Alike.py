class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ('a', 'e', 'i', 'o', 'u')
        a_count = 0
        b_count = 0
        s = s.lower()
        a = s[:len(s)//2]
        b = s[len(s)//2:]
        for vowel in vowels:
            a_count += a.count(vowel)
            b_count += b.count(vowel)
        return a_count == b_count
