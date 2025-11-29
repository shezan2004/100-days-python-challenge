import unittest

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = []
        i = len(a) - 1
        j = len(b) - 1
        carry = 0

        while i >= 0 or j >= 0 or carry:
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0

            current_sum = digit_a + digit_b + carry

            result_digit = current_sum % 2
            
            carry = current_sum // 2

            result.append(str(result_digit))

            i -= 1
            j -= 1
        
        return "".join(result[::-1])