class Solution(object):
    def integerBreak(self, n):
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        res = 1
        while n > 4:
            res *= 3
            n -= 3
        
        return res * n

# Test Cases
sol = Solution()
print(sol.integerBreak(2))   # Output: 1  (Explanation: 1 + 1)
print(sol.integerBreak(3))   # Output: 2  (Explanation: 2 + 1)
print(sol.integerBreak(4))   # Output: 4  (Explanation: 2 + 2)
print(sol.integerBreak(10))  # Output: 36 (Explanation: 3 + 3 + 4)
print(sol.integerBreak(58))  # Output: 1549681956