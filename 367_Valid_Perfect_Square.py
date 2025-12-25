class Solution(object):
    def isPerfectSquare(self, num):
        left = 1
        right = num

        while left <= right:
            mid = (left + right) // 2
            square = mid * mid

            if square == num:
                return True
            elif square < num:
                left = mid + 1
            else:
                right = mid - 1

        return False
s = Solution()

print(s.isPerfectSquare(1))    # True  -> 1 * 1
print(s.isPerfectSquare(4))    # True  -> 2 * 2
print(s.isPerfectSquare(9))    # True  -> 3 * 3
print(s.isPerfectSquare(16))   # True  -> 4 * 4
print(s.isPerfectSquare(25))   # True  -> 5 * 5

print(s.isPerfectSquare(2))    # False
print(s.isPerfectSquare(3))    # False
print(s.isPerfectSquare(14))   # False
print(s.isPerfectSquare(26))   # False

print(s.isPerfectSquare(2147395600))  # True  -> 46340 * 46340
