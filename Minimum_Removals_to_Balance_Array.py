class Solution(object):
    def minRemoval(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Sort the array to make the min/max relationship linear
        nums.sort()
        n = len(nums)
        
        max_kept = 0
        left = 0
        
        # Expand the window with 'right'
        for right in range(n):
            # If the current window violates the condition, 
            # shrink it from the left
            while nums[right] > nums[left] * k:
                left += 1
            
            # Update the maximum number of elements we can keep
            current_window_size = right - left + 1
            if current_window_size > max_kept:
                max_kept = current_window_size
                
        # The result is the total elements minus the ones we kept
        return n - max_kept