class Solution(object):
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))

if __name__ == "__main__":
    solution = Solution()

    nums1_ex1 = [1, 2, 2, 1]
    nums2_ex1 = [2, 2]
    print("Test Case 1 Output:", solution.intersection(nums1_ex1, nums2_ex1))
    
    nums1_ex2 = [4, 9, 5]
    nums2_ex2 = [9, 4, 9, 8, 4]
    print("Test Case 2 Output:", solution.intersection(nums1_ex2, nums2_ex2))
    
    nums1_ex3 = [1, 2, 3]
    nums2_ex3 = [4, 5, 6]
    print("Test Case 3 Output:", solution.intersection(nums1_ex3, nums2_ex3))