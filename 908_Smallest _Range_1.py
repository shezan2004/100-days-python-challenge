class Solution(object):
    def smallestRangeI(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return max(0, max(nums) - min(nums) - 2 * k)
    
    
    # Test case 1
nums = [1, 3, 6]
k = 3
# max = 6, min = 1 → range = 5
# after adjustment: 5 - 6 = -1 → answer = 0
print(Solution().smallestRangeI(nums, k))  # Expected: 0

# Test case 2
nums = [0, 10]
k = 2
# range = 10
# after adjustment: 10 - 4 = 6
print(Solution().smallestRangeI(nums, k))  # Expected: 6

# Test case 3
nums = [1]
k = 0
# only one element, range is always 0
print(Solution().smallestRangeI(nums, k))  # Expected: 0

# Test case 4
nums = [4, 7, 9]
k = 1
# range = 5
# after adjustment: 5 - 2 = 3
print(Solution().smallestRangeI(nums, k))  # Expected: 3

