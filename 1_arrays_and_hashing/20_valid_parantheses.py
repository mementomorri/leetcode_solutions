"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.



Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false



Constraints:

    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.
"""


def isValid_initial(s: str) -> bool:
    square_bracket = False
    round_bracket = False
    curly_bracket = False
    for bracket in s:
        match bracket:
            case '(':
                round_bracket = True
            case ')':
                round_bracket = False
            case '[':
                square_bracket = True
            case ']':
                square_bracket = False
            case '{':
                curly_bracket = True
            case '}':
                curly_bracket = False
    return square_bracket + round_bracket + curly_bracket == 0


def isValid(s: str) -> bool:
    brackets = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    bracket_stack = []
    for bracket in s:
        if bracket_stack and bracket_stack[-1] in brackets and bracket == brackets[bracket_stack[-1]]:
            bracket_stack.pop()
        else:
            bracket_stack.append(bracket)
    return not bracket_stack


if __name__ == '__main__':
    print(isValid(s="()"))
    print(isValid(s="()[]{}"))
    print(isValid(s="(]"))
    print(isValid(s="([)]"))
    print(isValid(s="{[]}"))
