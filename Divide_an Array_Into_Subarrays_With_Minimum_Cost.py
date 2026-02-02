class Solution(object):
    def minimumCost(self, nums):
        n = len(nums)
        
        # If exactly 3 elements, each must be its own subarray
        if n == 3:
            return nums[0] + nums[1] + nums[2]
        
        # Build suffix minimum array
        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]
        
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])
        
        ans = float('inf')
        
        # Try all valid starting points of the second subarray
        for i in range(1, n - 1):
            ans = min(ans, nums[i] + suffix_min[i + 1])
        
        return nums[0] + ans