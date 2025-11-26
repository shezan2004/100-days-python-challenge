class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                low = mid + 1
            
            else:
                high = mid - 1
        
        return low

# --- Test Cases ---

if __name__ == '__main__':
    # Initialize the Solution class
    sol = Solution()

    # Define test cases as a list of tuples: (nums, target, expected_output)
    test_cases = [
        ([1, 3, 5, 6], 5, 2),    # Found
        ([1, 3, 5, 6], 2, 1),    # Insert middle
        ([1, 3, 5, 6], 7, 4),    # Insert end
        ([1, 3, 5, 6], 0, 0),    # Insert start
        ([10, 20, 30, 40, 50], 30, 2), # Longer array, found
        ([10, 20, 40, 50], 35, 2), # Longer array, insert
        ([1], 1, 0),             # Single element, found
        ([1], 2, 1),             # Single element, insert end
        ([1], 0, 0)              # Single element, insert start
    ]

    print("--- Running Search Insert Test Suite ---")
    
    all_passed = True
    for i, (nums, target, expected) in enumerate(test_cases, 1):
        result = sol.searchInsert(nums, target)
        
        # Check if the result matches the expected output
        if result == expected:
            status = "✅ PASSED"
        else:
            status = "❌ FAILED"
            all_passed = False
            
        print(f"\nTest {i}: {status}")
        print(f"  Input: nums={nums}, target={target}")
        print(f"  Expected: {expected}, Got: {result}")

    print("\n----------------------------------------")
    if all_passed:
        print("🎉 All test cases passed successfully!")
    else:
        print("🛑 Some test cases failed. Review the implementation.")
    print("----------------------------------------")