class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0
# Test cases
s = Solution()

print(s.canWinNim(1))   # True  (take 1, win)
print(s.canWinNim(2))   # True  (take 2, win)
print(s.canWinNim(3))   # True  (take 3, win)
print(s.canWinNim(4))   # False (losing position)
print(s.canWinNim(5))   # True  (leave 4)
print(s.canWinNim(8))   # False (multiple of 4)
print(s.canWinNim(10))  # True
print(s.canWinNim(16))  # False
print(s.canWinNim(231 - 1))  # True (large non-multiple of 4)
