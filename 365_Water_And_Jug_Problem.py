class Solution(object):
    def canMeasureWater(self, x, y, target):
        if target > x + y:
            return False

        if target == 0:
            return True

        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        return target % gcd(x, y) == 0
