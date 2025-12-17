class Solution(object):
    def addStrings(self, num1, num2):
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            digit1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            digit2 = ord(num2[j]) - ord('0') if j >= 0 else 0

            total = digit1 + digit2 + carry
            carry = total // 10
            result.append(chr((total % 10) + ord('0')))

            i -= 1
            j -= 1

        return ''.join(reversed(result))

sol = Solution()

print(sol.addStrings("11", "123"))    # Expected: "134"
print(sol.addStrings("456", "77"))    # Expected: "533"
print(sol.addStrings("0", "0"))       # Expected: "0"
print(sol.addStrings("999", "1"))     # Expected: "1000"
print(sol.addStrings("1", "9999"))    # Expected: "10000"
