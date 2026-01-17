class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        head = 1
        step = 1
        remaining = n
        left = True

        while remaining > 1:
            if left or remaining % 2 == 1:
                head += step

            remaining //= 2
            step *= 2
            left = not left

        return head
# Test cases
s = Solution()

print(s.lastRemaining(1))   # Expected: 1
print(s.lastRemaining(2))   # Expected: 2
print(s.lastRemaining(3))   # Expected: 2
print(s.lastRemaining(4))   # Expected: 2
print(s.lastRemaining(5))   # Expected: 2
print(s.lastRemaining(6))   # Expected: 4
print(s.lastRemaining(9))   # Expected: 6
print(s.lastRemaining(10))  # Expected: 8
print(s.lastRemaining(100)) # Expected: 54
