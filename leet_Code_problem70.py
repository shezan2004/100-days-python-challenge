# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
class Solution(object):
    def climbStairs(self, n):
        if n <= 2:
            return n

        a = 1   # ways to climb to step 1
        b = 2   # ways to climb to step 2

        for _ in range(3, n + 1):
            a, b = b, a + b   # Fibonacci update

        return b
