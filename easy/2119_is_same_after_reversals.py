"""
Reversing an integer means to reverse all its digits.

    For example, reversing 2021 gives 1202. Reversing 12300 gives 321 as the leading zeros are not retained.

Given an integer num, reverse num to get reversed1, then reverse reversed1 to get reversed2. Return true if reversed2 equals num. Otherwise return false.

 

Example 1:

Input: num = 526
Output: true
Explanation: Reverse num to get 625, then reverse 625 to get 526, which equals num.

Example 2:

Input: num = 1800
Output: false
Explanation: Reverse num to get 81, then reverse 81 to get 18, which does not equal num.

Example 3:

Input: num = 0
Output: true
Explanation: Reverse num to get 0, then reverse 0 to get 0, which equals num.

 

Constraints:

    0 <= num <= 106
"""

def is_same_after_reversals(num: int) -> bool:
    return num == 0 or not (num % 10 == 0)

if __name__ == '__main__':
    print('num = 526')
    res1 = is_same_after_reversals(num=526)
    assert res1 == True, res1
    print('\n')

    print('num = 1800')
    res2 = is_same_after_reversals(num=1800)
    assert res2 == False, res2
    print( '\n')

    print('num = 0')
    res3 = is_same_after_reversals(num=0)
    assert res3 == True, res3
    print('\n')

