class Solution(object):
    def superPow(self, a, b):
        MOD = 1337

        def modPow(x, n):
            result = 1
            x %= MOD
            while n > 0:
                if n % 2 == 1:
                    result = (result * x) % MOD
                x = (x * x) % MOD
                n //= 2
            return result

        result = 1
        for digit in b:
            result = modPow(result, 10)
            result = (result * modPow(a, digit)) % MOD

        return result
class Solution(object):
    def superPow(self, a, b):
        MOD = 1337

        def modPow(x, n):
            result = 1
            x %= MOD
            while n > 0:
                if n % 2 == 1:
                    result = (result * x) % MOD
                x = (x * x) % MOD
                n //= 2
            return result

        result = 1
        for digit in b:
            result = modPow(result, 10)
            result = (result * modPow(a, digit)) % MOD

        return result

solution = Solution()

# Example 1
a = 2
b = [3]
print(solution.superPow(a, b))  # Expected: 8

# Example 2
a = 2
b = [1, 0]
print(solution.superPow(a, b))  # Expected: 1024

# Example 3
a = 1
b = [4, 3, 3, 8, 5, 2]
print(solution.superPow(a, b))  # Expected: 1

# Additional edge cases
a = 2147483647
b = [2, 0, 0]
print(solution.superPow(a, b))  # Large a, large exponent

a = 5
b = [0]
print(solution.superPow(a, b))  # Expected: 1
