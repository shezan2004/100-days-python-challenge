class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = {}
        
        # Count occurrences
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        unique_sum = 0
        
        # Sum only numbers that appear exactly once
        for num in counts:
            if counts[num] == 1:
                unique_sum += num
                
        return unique_sum

if __name__ == "__main__":
    solver = Solution()

    nums1 = [1, 2, 3, 2]
    result1 = solver.sumOfUnique(nums1)
    print(f"Test Case 1: Input: {nums1} -> Output: {result1} (Expected: 4)")

    nums2 = [1, 1, 1, 1, 1]
    result2 = solver.sumOfUnique(nums2)
    print(f"Test Case 2: Input: {nums2} -> Output: {result2} (Expected: 0)")

    nums3 = [1, 2, 3, 4, 5]
    result3 = solver.sumOfUnique(nums3)
    print(f"Test Case 3: Input: {nums3} -> Output: {result3} (Expected: 15)")
 
    nums4 = [10]
    result4 = solver.sumOfUnique(nums4)
    print(f"Test Case 4: Input: {nums4}  -> Output: {result4} (Expected: 10)")
    
    nums5 = [10, 6, 9, 6, 9, 10, 8]
    result5 = solver.sumOfUnique(nums5)
    print(f"Test Case 5: Input: {nums5} -> Output: {result5} (Expected: 8)")