"""
A password is said to be strong if it satisfies all the following criteria:

    It has at least 8 characters.
    It contains at least one lowercase letter.
    It contains at least one uppercase letter.
    It contains at least one digit.
    It contains at least one special character. The special characters are the characters in the following string: "!@#$%^&*()-+".
    It does not contain 2 of the same character in adjacent positions (i.e., "aab" violates this condition, but "aba" does not).

Given a string password, return true if it is a strong password. Otherwise, return false.



Example 1:

Input: password = "IloveLe3tcode!"
Output: true
Explanation: The password meets all the requirements. Therefore, we return true.

Example 2:

Input: password = "Me+You--IsMyDream"
Output: false
Explanation: The password does not contain a digit and also contains 2 of the same character in adjacent positions. Therefore, we return false.

Example 3:

Input: password = "1aB!"
Output: false
Explanation: The password does not meet the length requirement. Therefore, we return false.



Constraints:

    1 <= password.length <= 100
    password consists of letters, digits, and special characters: "!@#$%^&*()-+".


"""
import string


class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        low_case = False
        upp_case = False
        digit = False
        special_char = False

        special_characters = "!@#$%^&*()-+"
        nums = "0123456789"
        last_char = ''

        if len(password) < 8:
            return False

        for idx in range(len(password)):
            if password[idx] == last_char:
                return False
            last_char = password[idx]
            if not False in (low_case, upp_case, digit, special_char):
                continue
            if password[idx] in string.ascii_lowercase:
                low_case = True
            if password[idx] in string.ascii_uppercase:
                upp_case = True
            if password[idx] in nums:
                digit = True
            if password[idx] in special_characters:
                special_char = True

        return not False in (low_case, upp_case, digit, special_char)

