class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"

        if num < 0:
            num += 1 << 32

        digits = "0123456789abcdef"
        result = ""

        while num > 0:
            remainder = num % 16
            result = digits[remainder] + result
            num //= 16

        return result
solution = Solution()

print(solution.toHex(26))        # expected: "1a"
print(solution.toHex(-1))        # expected: "ffffffff"
print(solution.toHex(0))         # expected: "0"
print(solution.toHex(16))        # expected: "10"
print(solution.toHex(255))       # expected: "ff"
print(solution.toHex(-16))       # expected: "fffffff0"
print(solution.toHex(2147483647)) # expected: "7fffffff"
print(solution.toHex(-2147483648)) # expected: "80000000"
