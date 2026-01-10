class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 0:
            n //= 5
            count += n
        return count
    
solution = Solution()

print(solution.trailingZeroes(3))    # Expected output: 0
print(solution.trailingZeroes(5))    # Expected output: 1
print(solution.trailingZeroes(0))    # Expected output: 0
print(solution.trailingZeroes(10))   # Expected output: 2
print(solution.trailingZeroes(25))   # Expected output: 6
print(solution.trailingZeroes(100))  # Expected output: 24
