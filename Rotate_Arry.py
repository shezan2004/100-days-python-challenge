class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n  # handle large k

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # reverse whole array
        reverse(0, n - 1)
        # reverse first k elements
        reverse(0, k - 1)
        # reverse remaining elements
        reverse(k, n - 1)
