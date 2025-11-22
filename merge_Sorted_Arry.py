class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1

        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            
            p -= 1

# --- Test Runner Code ---

def run_test(nums1_orig, m, nums2, n, expected):
    # Deep copy to ensure the original list isn't modified by previous tests
    nums1_copy = list(nums1_orig) 
    
    # Create an instance of the Solution class
    solver = Solution()
    
    # Run the merge operation in-place
    solver.merge(nums1_copy, m, nums2, n)
    
    # Check the result
    assert nums1_copy == expected, f"Input: nums1={nums1_orig}, m={m}, nums2={nums2}, n={n} | Expected: {expected} | Got: {nums1_copy}"
    print(f"Test Passed! Input: nums1={nums1_orig} -> Result: {nums1_copy}")

# --- Test Cases ---

print("Running Tests for Merge Sorted Array:\n")

# 1. Standard Case (Example 1)
run_test([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6])

# 2. nums2 is empty (Example 2)
run_test([1], 1, [], 0, [1])

# 3. nums1 is empty (Example 3)
run_test([0], 0, [1], 1, [1])

# 4. nums1 elements are all greater than nums2 elements
run_test([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3, [1, 2, 3, 4, 5, 6])

# 5. nums2 elements are all greater than nums1 elements
run_test([1, 2, 3, 0, 0, 0], 3, [4, 5, 6], 3, [1, 2, 3, 4, 5, 6])

# 6. Single element arrays
run_test([2, 0], 1, [1], 1, [1, 2])

# 7. Duplicates and zeros (complex scenario)
run_test([10, 20, 30, 0, 0, 0, 0], 3, [5, 10, 15, 20], 4, [5, 10, 10, 15, 20, 20, 30])