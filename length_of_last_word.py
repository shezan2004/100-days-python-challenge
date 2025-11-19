class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # This is the logic that solves the problem
        return len(s.split()[-1])

# --- The driver code goes below the class ---
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case
    test_string = "   fly me   to   the moon  "
    result = solution.lengthOfLastWord(test_string)
    
    print(f"Input: '{test_string}'")
    print(f"Length of last word: {result}")