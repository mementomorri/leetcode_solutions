"""
You are given an integer array digits, where each element is a digit. The array may contain duplicates.

You need to find all the unique integers that follow the given requirements:

    The integer consists of the concatenation of three elements from digits in any arbitrary order.
    The integer does not have leading zeros.
    The integer is even.

For example, if the given digits were [1, 2, 3], integers 132 and 312 follow the requirements.

Return a sorted array of the unique integers.



Example 1:

Input: digits = [2,1,3,0]
Output: [102,120,130,132,210,230,302,310,312,320]
Explanation: All the possible integers that follow the requirements are in the output array.
Notice that there are no odd integers or integers with leading zeros.

Example 2:

Input: digits = [2,2,8,8,2]
Output: [222,228,282,288,822,828,882]
Explanation: The same digit can be used as many times as it appears in digits.
In this example, the digit 8 is used twice each time in 288, 828, and 882.

Example 3:

Input: digits = [3,7,5]
Output: []
Explanation: No even integers can be formed using the given digits.



Constraints:

    3 <= digits.length <= 100
    0 <= digits[i] <= 9
"""


from typing import List


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        even_nums = False
        for n in digits:
            if n % 2 == 0:
                even_nums = True
                break
        if not even_nums and 0 not in digits:
            return []
        result = set()
        digits_len = len(digits)
        for n1 in range(digits_len):
            if digits[n1] != 0:
                for n2 in range(digits_len):
                    for n3 in range(digits_len):
                        if n1 != n2 and n1 != n3 and n2 != n3 and digits[n3] % 2 == 0:
                            result.add(digits[n1] * 100 + digits[n2] * 10 + digits[n3])
        return sorted(list(result))


if __name__ == '__main__':
    sol = Solution()
    print(sol.findEvenNumbers([2, 1, 3, 0]))
    print(sol.findEvenNumbers([2, 2, 8, 8, 2]))
    print(sol.findEvenNumbers([3, 7, 5]))
