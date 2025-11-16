
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # A dictionary to store the numbers we have seen so far
        # The key is the number, and the value is its index
        seen = {}

        # Use enumerate to get both the index (i) and the value (val)
        for i, val in enumerate(nums):
            # Calculate the complement (the value we need to find)
            complement = target - val
            
            # Check if the complement is already in our dictionary
            if complement in seen:
                # If it is, we found the solution!
                # Return the complement's index (from the 'seen' map)
                # and the current number's index (i)
                return [seen[complement], i]
            
            # If the complement wasn't found, add the current number
            # and its index to the 'seen' map for future checks.
            # We add it *after* the check to avoid using the same element twice.
            seen[val] = i

# \/\/\/ ADD THIS CODE BELOW \/\/\/

# This special block runs code only when the file is executed directly
if __name__ == "__main__":
    # 1. Create an instance of the Solution
    s = Solution()
    
    # 2. Define your input data (from Example 1)
    nums_input = [2, 7, 11, 15]
    target_input = 9
    
    # 3. Call the method and store the result
    result = s.twoSum(nums_input, target_input)
    
    # 4. Print the result to the terminal
    print(result)

    # You can also test Example 2
    nums_input_2 = [3, 2, 4]
    target_input_2 = 6
    print(s.twoSum(nums_input_2, target_input_2))