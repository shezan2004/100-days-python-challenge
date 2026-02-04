class Solution(object):
    def isTrionic(self, nums):
        n = len(nums)
        # We need at least 4 elements to satisfy 0 < p < q < n-1
        if n < 4:
            return False
        
        i = 0
        
        # Phase 1: Strictly Increasing to Peak p
        while i + 1 < n and nums[i] < nums[i+1]:
            i += 1
        
        # Peak p cannot be the start (index 0) or the very end (n-1)
        if i == 0 or i == n - 1:
            return False
        
        p = i
        
        # Phase 2: Strictly Decreasing to Valley q
        while i + 1 < n and nums[i] > nums[i+1]:
            i += 1
            
        # Valley q must be after p and cannot be the end of the array
        if i == p or i == n - 1:
            return False
            
        q = i
        
        # Phase 3: Strictly Increasing to the End
        while i + 1 < n and nums[i] < nums[i+1]:
            i += 1
            
        # If we reached the final index n-1, it's a Trionic Array
        return i == n - 1