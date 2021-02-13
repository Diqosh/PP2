class Solution:
    def isPalindrome(self, x: int) -> bool:
        strg = str(x)
        return True if strg == strg[::-1] else False