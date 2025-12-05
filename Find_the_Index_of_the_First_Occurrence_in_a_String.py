class Solution(object):
    def strStr(self, haystack, needle):
        N = len(haystack)
        M = len(needle)

        if M > N:
            return -1

        for i in range(N - M + 1):
            if haystack[i : i + M] == needle:
                return i

        return -1

# --- Test Case ---

solution = Solution()

# Test 3: Needle at the end of haystack
haystack_3 = "mississippi"
needle_3 = "pi"
expected_output_3 = 9
actual_output_3 = solution.strStr(haystack_3, needle_3)

print(f"Haystack: '{haystack_3}'")
print(f"Needle: '{needle_3}'")
print(f"Expected Output: {expected_output_3}")
print(f"Actual Output: {actual_output_3}")
print(f"Result: {'PASS' if actual_output_3 == expected_output_3 else 'FAIL'}")