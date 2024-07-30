"""
You are given a string s consisting only of characters 'a' and 'b'.

You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

Return the minimum number of deletions needed to make s balanced.



Example 1:

Input: s = "aababbab"
Output: 2
Explanation: You can either:
Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").

Example 2:

Input: s = "bbaaaaabb"
Output: 2
Explanation: The only solution is to delete the first two characters.



Constraints:

    1 <= s.length <= 105
    s[i] is 'a' or 'b'.
"""


class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_count_right = s.count("a")
        b_count_left = 0
        res = len(s)
        for c in s:
            a_count_right -= 1 if c == "a" else 0
            res = min(res, b_count_left + a_count_right)
            b_count_left += 1 if c == "b" else 0
        return res
