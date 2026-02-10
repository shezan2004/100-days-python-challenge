class Solution(object):
    def longestBalanced(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_length = 0
        n = len(nums)
        
        # Iterate over every possible starting point
        for i in range(n):
            seen_even = set()
            seen_odd = set()
            
            # Expand the subarray from index i to j
            for j in range(i, n):
                num = nums[j]
                
                if num % 2 == 0:
                    seen_even.add(num)
                else:
                    seen_odd.add(num)
                
                # Check if the counts of distinct numbers match
                if len(seen_even) == len(seen_odd):
                    max_length = max(max_length, j - i + 1)
                        
        return max_length