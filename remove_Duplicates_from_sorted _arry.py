class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        # i is the slow pointer, marking the position for the next unique element.
        i = 0
        
        # j is the fast pointer, iterating through the array.
        for j in range(1, len(nums)):
            
            # If a new unique element is found (nums[j] != nums[i])
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        
        # The number of unique elements (k) is i + 1.
        k = i + 1
        return k

# --- Test Cases ---

def run_test(nums, expected_k, expected_nums_prefix):
    """Runs a test case and prints the result."""
    solution = Solution()
    original_nums = list(nums)  # Save original list for printing
    k = solution.removeDuplicates(nums)
    
    # Check if the returned length (k) is correct
    k_match = (k == expected_k)
    
    # Check if the modified prefix matches the expected unique elements
    prefix_match = (nums[:k] == expected_nums_prefix)
    
    print(f"Input: {original_nums}")
    print(f"Returned k: {k} (Expected: {expected_k}) -> {'PASS' if k_match else 'FAIL'}")
    print(f"Modified nums (first {k} elements): {nums[:k]}")
    print(f"Expected prefix: {expected_nums_prefix} -> {'PASS' if prefix_match else 'FAIL'}")
    print(f"Final state of nums: {nums}")
    print("-" * 30)


print("--- Running Tests for removeDuplicates ---")

# Example 1: Standard case
nums_1 = [1, 1, 2]
expected_k_1 = 2
expected_prefix_1 = [1, 2]
run_test(nums_1, expected_k_1, expected_prefix_1)

# Example 2: Many duplicates
nums_2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
expected_k_2 = 5
expected_prefix_2 = [0, 1, 2, 3, 4]
run_test(nums_2, expected_k_2, expected_prefix_2)

# Example 3: No duplicates
nums_3 = [10, 20, 30, 40]
expected_k_3 = 4
expected_prefix_3 = [10, 20, 30, 40]
run_test(nums_3, expected_k_3, expected_prefix_3)

# Example 4: All duplicates
nums_4 = [5, 5, 5, 5]
expected_k_4 = 1
expected_prefix_4 = [5]
run_test(nums_4, expected_k_4, expected_prefix_4)

# Example 5: Empty list
nums_5 = []
expected_k_5 = 0
expected_prefix_5 = []
run_test(nums_5, expected_k_5, expected_prefix_5)