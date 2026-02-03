from sortedcontainers import SortedList

class Solution(object):
    def minimumCost(self, nums, k, dist):
        n = len(nums)
        target_count = k - 1
        
        # Initialize window with elements from index 1 to dist + 1
        window = SortedList(nums[1 : dist + 2])
        current_sum = sum(window[:target_count])
        ans = nums[0] + current_sum
        
        for i in range(2, n - dist):
            # 1. Remove the element sliding out
            old_val = nums[i - 1]
            idx = window.index(old_val)
            if idx < target_count:
                current_sum -= old_val
                # Only add the next available element if it exists
                if len(window) > target_count:
                    current_sum += window[target_count]
            window.remove(old_val)
            
            # 2. Add the element sliding in
            new_val = nums[i + dist]
            window.add(new_val)
            idx = window.bisect_left(new_val)
            if idx < target_count:
                current_sum += new_val
                # Only subtract if there was an element pushed out of the top k-1
                if len(window) > target_count:
                    current_sum -= window[target_count]
            
            ans = min(ans, nums[0] + current_sum)
            
        return ans