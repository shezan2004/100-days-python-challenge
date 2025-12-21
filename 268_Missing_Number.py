class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        return (n * (n + 1) // 2) - sum(nums)

# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.missingNumber([3, 0, 1]))                   # 2
    print(sol.missingNumber([0, 1]))                      # 2
    print(sol.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1])) # 8