class Solution:
    def reverse(self, x: int) -> int:
        strg = str(x)
        if x >= 0:
            strg = strg[::-1]
        else:
            strg = strg[1:]
            strg = '-' + strg[::-1]
        return int(strg) if -2**31 <= int(strg) <= 2**(31) - 1 else 0
