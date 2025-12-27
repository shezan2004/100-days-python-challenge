class Solution(object):
    def isPowerOfFour(self, n):
        if n <= 0:
            return False
        
        if n & (n - 1) != 0:
            return False
        return (n & 0x55555555) != 0
# Test cases
solution = Solution()

print(solution.isPowerOfFour(16))   # True  (4^2)
print(solution.isPowerOfFour(5))    # False
print(solution.isPowerOfFour(1))    # True  (4^0)
print(solution.isPowerOfFour(4))    # True  (4^1)
print(solution.isPowerOfFour(64))   # True  (4^3)
print(solution.isPowerOfFour(0))    # False
print(solution.isPowerOfFour(-4))   # False
print(solution.isPowerOfFour(2))    # False
print(solution.isPowerOfFour(8))    # False
print(solution.isPowerOfFour(1024)) # True  (4^5)
