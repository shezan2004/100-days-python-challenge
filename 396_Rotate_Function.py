class Solution(object):
    def maxRotateFunction(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        totalSum = sum(nums)
        
        # Compute F(0)
        curr = 0
        for i in range(n):
            curr += i * nums[i]
        
        ans = curr
        
        # Compute F(1) to F(n-1)
        for k in range(1, n):
            curr = curr + totalSum - n * nums[n - k]
            ans = max(ans, curr)
        
        return ans
