class Solution(object):
    def isPalindrome(self, x):
        """
        Checks if an integer x is a palindrome without converting it to a string.
        :type x: int
        :rtype: bool
        """
        # Handle special cases:
        # 1. Negative numbers are not palindromes.
        # 2. Numbers ending in 0 (except 0 itself) are not palindromes (e.g., 10, 120).
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reverted_number = 0
        
        # Stop when we've processed about half the digits
        while x > reverted_number:
            # Build the reversed number
            reverted_number = reverted_number * 10 + x % 10
            # Remove the last digit from x
            x //= 10
            
        # For even length (e.g., 1221): x == reverted_number (12 == 12)
        # For odd length (e.g., 121): x == reverted_number // 10 (1 == 12 // 10 -> 1 == 1)
        return x == reverted_number or x == reverted_number // 10

# --- Test Cases ---

def run_tests():
    solver = Solution()
    
    # Define test cases: (input, expected_output, description)
    test_cases = [
        # Palindromes
        (121, True, "Odd-Digit Palindrome"),
        (1221, True, "Even-Digit Palindrome"),
        (0, True, "Zero"),
        (1, True, "Single Digit"),
        (1000001, True, "Large with Internal Zeros"),
        
        # Non-Palindromes (Edge Cases)
        (-121, False, "Negative Number"),
        (10, False, "Ends in Zero (Non-zero)"),
        (123, False, "Standard Non-Palindrome"),
        (100, False, "Multiple Zeros at End"),
        (2147483647, False, "Max 32-bit Integer") # Example of a large non-palindrome
    ]
    
    print("--- Running Palindrome Tests ---")
    all_passed = True
    
    for x, expected, desc in test_cases:
        actual = solver.isPalindrome(x)
        
        if actual == expected:
            status = "✅ PASSED"
        else:
            status = f"❌ FAILED (Expected: {expected}, Got: {actual})"
            all_passed = False
            
        print(f"Test Case: {desc} (Input: {x}) -> {status}")

    print("---------------------------------")
    if all_passed:
        print("🎉 All tests passed successfully!")
    else:
        print("🛑 Some tests failed.")

if __name__ == "__main__":
    run_tests()