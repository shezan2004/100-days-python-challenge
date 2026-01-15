class Solution(object):
    def checkSubarraySum(self, nums, k):
        remainder_index = {0: -1}
        running_sum = 0

        for i in range(len(nums)):
            running_sum += nums[i]
            rem = running_sum % k

            if rem in remainder_index:
                if i - remainder_index[rem] >= 2:
                    return True
            else:
                remainder_index[rem] = i

        return False
