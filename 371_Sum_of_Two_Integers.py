# Given two integers a and b, return the sum of the two integers without using the operators + and -
class Solution(object):
    def getSum(self, a, b):
        
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask

        return a if a <= max_int else ~(a ^ mask)
