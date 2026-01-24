class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1

        total = 10          # count for n = 1
        unique = 9          # choices for the first digit (1–9)
        available = 9       # remaining digits

        for i in range(2, n + 1):
            unique *= available
            total += unique
            available -= 1

        return total
