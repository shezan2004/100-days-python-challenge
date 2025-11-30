class Solution:
    def plusOne(self, digits):
        n = len(digits)

        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        return [1] + digits


# test code
s = Solution()
print(s.plusOne([1, 2, 3]))    # [1, 2, 4]
print(s.plusOne([4, 3, 2, 1])) # [4, 3, 2, 2]
print(s.plusOne([9]))          # [1, 0]
print(s.plusOne([9, 9, 9]))    # [1, 0, 0, 0]
print(s.plusOne([8, 9, 9]))    # [9, 0, 0]
