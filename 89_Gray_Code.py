class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        limit = 1 << n  # 2^n

        for i in range(limit):
            result.append(i ^ (i >> 1))

        return result


# ---------- Test cases ----------
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    n = 1
    print("n = 1")
    print(sol.grayCode(n))  # Expected: [0, 1]

    # Test case 2
    n = 2
    print("\nn = 2")
    print(sol.grayCode(n))  # Expected: [0, 1, 3, 2]

    # Test case 3
    n = 3
    print("\nn = 3")
    print(sol.grayCode(n))
    # One valid output:
    # [0, 1, 3, 2, 6, 7, 5, 4]

    # Test case 4 (edge of practicality)
    n = 4
    print("\nn = 4")
    print(sol.grayCode(n))
