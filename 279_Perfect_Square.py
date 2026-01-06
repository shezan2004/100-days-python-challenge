class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp[i] will store the least number of perfect squares that sum to i
        dp = [0] + [float('inf')] * n

        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1

        return dp[n]

# Test cases
s = Solution()

print(s.numSquares(1))    # 1 -> 1
print(s.numSquares(2))    # 2 -> 1 + 1
print(s.numSquares(3))    # 3 -> 1 + 1 + 1
print(s.numSquares(4))    # 1 -> 4
print(s.numSquares(12))   # 3 -> 4 + 4 + 4
print(s.numSquares(13))   # 2 -> 4 + 9
print(s.numSquares(17))   # 2 -> 16 + 1
print(s.numSquares(23))   # 4 -> 9 + 9 + 4 + 1
print(s.numSquares(100))  # 1 -> 100
