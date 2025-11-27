class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []

        triangle = [[1]]

        for i in range(1, numRows):
            prev_row = triangle[-1]
            new_row = [1]

            for j in range(1, i):
                new_element = prev_row[j - 1] + prev_row[j]
                new_row.append(new_element)

            new_row.append(1)

            triangle.append(new_row)

        return triangle

## 🧪 Test Case Insertion

# 1. Create an instance of the Solution class
solver = Solution()

# 2. Define the Input and Expected Output
test_input = 4
# Expected Output:
# Row 1: [1]
# Row 2: [1, 1]
# Row 3: [1, 2, 1]
# Row 4: [1, 3, 3, 1]
expected_output = [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1]
]

# 3. Call the function and get the actual output
actual_output = solver.generate(test_input)

# 4. Assert/Print the result
print(f"Input (numRows): {test_input}")
print(f"Expected Output: {expected_output}")
print(f"Actual Output:   {actual_output}")

# Check if the result is correct
assert actual_output == expected_output, f"Test failed! Expected {expected_output}, but got {actual_output}"
