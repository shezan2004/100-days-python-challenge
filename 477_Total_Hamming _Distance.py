class Solution(object):
    def totalHammingDistance(self, nums):
        total = 0
        n = len(nums)
        
        for bit in range(30):  # enough for numbers up to 10^9
            ones = 0
            for num in nums:
                if (num >> bit) & 1:
                    ones += 1
            zeros = n - ones
            total += ones * zeros
        
        return total
# Test Case 1: Given example
nums = [4, 14, 2]
# Expected output: 6

# Test Case 2: Repeated numbers
nums = [4, 14, 4]
# Expected output: 4

# Test Case 3: All elements are the same
nums = [7, 7, 7]
# Expected output: 0

# Test Case 4: Single element (no pairs)
nums = [0]
# Expected output: 0

# Test Case 5: Two numbers
nums = [1, 2]
# Binary: 01 and 10
# Expected output: 2

# Test Case 6: Large values
nums = [0, 10**9]
# Expected output: number of 1s in binary of 10**9
