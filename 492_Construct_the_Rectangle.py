class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        w = int(area ** 0.5)

        while area % w != 0:
            w -= 1

        l = area // w
        return [l, w]


# Test cases
solution = Solution()

test_cases = [
    1,
    2,
    3,
    4,
    9,
    10,
    16,
    37,
    100,
    122122,
    10000000
]

for area in test_cases:
    result = solution.constructRectangle(area)
    print("Input area:", area, "Output:", result)
