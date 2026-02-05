class Solution(object):
    def constructTransformedArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [0] * n
        
        for i in range(n):
            if nums[i] == 0:
                result[i] = 0
            else:
                # Calculate the landing index using modulo
                # Python's % operator handles negative results by wrapping them
                landing_index = (i + nums[i]) % n
                result[i] = nums[landing_index]
                
        return result