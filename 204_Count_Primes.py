class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0

        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False

        p = 2
        while p * p < n:
            if is_prime[p]:
                for multiple in range(p * p, n, p):
                    is_prime[multiple] = False
            p += 1

        return sum(is_prime)
# Test cases
solution = Solution()

print(solution.countPrimes(10))    # Expected: 4  (2, 3, 5, 7)
print(solution.countPrimes(0))     # Expected: 0
print(solution.countPrimes(1))     # Expected: 0
print(solution.countPrimes(2))     # Expected: 0
print(solution.countPrimes(3))     # Expected: 1  (2)
print(solution.countPrimes(5))     # Expected: 2  (2, 3)
print(solution.countPrimes(20))    # Expected: 8  (2,3,5,7,11,13,17,19)
print(solution.countPrimes(100))   # Expected: 25
print(solution.countPrimes(1000))  # Expected: 168
