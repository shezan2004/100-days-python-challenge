import collections

class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        freq = collections.Counter(arr)
        
        max_lucky = -1
        
        for key, count in freq.items():
            if key == count:
                max_lucky = max(max_lucky, key)
                
        return max_lucky

def run_tests():
    sol = Solution()
    
    test_cases = [
        ([2, 2, 3, 4], 2, "Example 1"),
        ([1, 2, 2, 3, 3, 3], 3, "Example 2"),
        ([2, 2, 2, 3, 3], -1, "Example 3"),
        ([7, 7, 7, 7, 7, 7, 7], 7, "Edge Case 4: Perfect Match"),
        ([1, 1, 1, 1, 1, 1, 1], -1, "Edge Case 5: Mismatched 1s"),
        ([5], -1, "Edge Case 6: Single large element"),
        ([], -1, "Edge Case 7: Empty array"),
    ]
    
    print("--- Running Tests for findLucky ---")
    
    all_passed = True
    for arr, expected, name in test_cases:
        result = sol.findLucky(arr)
        
        if result == expected:
            status = "PASS"
        else:
            status = "FAIL"
            all_passed = False
            
        print(f"[{status}] {name}: Input: {arr}, Expected: {expected}, Got: {result}")

    if all_passed:
        print("\nAll tests passed successfully!")
    else:
        print("\nSome tests failed.")

if __name__ == "__main__":
    run_tests()