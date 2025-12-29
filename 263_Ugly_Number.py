class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        for p in (2, 3, 5):
            while n % p == 0:
                n //= p

        return n == 1
# Test cases
s = Solution()

print(s.isUgly(6))    # True   (2 × 3)
print(s.isUgly(1))    # True   (no prime factors)
print(s.isUgly(14))   # False  (includes 7)
print(s.isUgly(8))    # True   (2 × 2 × 2)
print(s.isUgly(0))    # False  (not positive)
print(s.isUgly(-5))   # False  (negative number)
print(s.isUgly(30))   # True   (2 × 3 × 5)
print(s.isUgly(25))   # True   (5 × 5)
print(s.isUgly(49))   # False  (7 × 7)
