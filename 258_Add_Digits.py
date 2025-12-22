class Solution(object):
    def addDigits(self, num):
        if num == 0:
            return 0
        return 1 + (num - 1) % 9
# Test cases
s = Solution()

print(s.addDigits(38))        # Expected: 2
print(s.addDigits(0))         # Expected: 0
print(s.addDigits(9))         # Expected: 9
print(s.addDigits(18))        # Expected: 9
print(s.addDigits(12345))     # Expected: 6  (1+2+3+4+5 = 15 → 1+5 = 6)
print(s.addDigits(999999))    # Expected: 9
print(s.addDigits(1))         # Expected: 1
print(s.addDigits(10))        # Expected: 1
