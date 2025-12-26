class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        result = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            digit = x % 10
            x //= 10

            if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > 7):
                return 0

            result = result * 10 + digit

        return sign * result
# Test cases
s = Solution()

print(s.reverse(123))        # 321
print(s.reverse(-123))       # -321
print(s.reverse(120))        # 21
print(s.reverse(0))          # 0
print(s.reverse(10))         # 1
print(s.reverse(-10))        # -1


print(s.reverse(1534236469)) 
print(s.reverse(1463847412)) 
print(s.reverse(-2147483648))
print(s.reverse(2147483647)) 
