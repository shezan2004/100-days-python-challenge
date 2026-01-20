class Solution(object):
    def nextGreaterElement(self, n):
        digits = list(str(n))
        
        # Step 1: find first decreasing digit from the right
        i = len(digits) - 2
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1
        
        if i < 0:
            return -1
        
        # Step 2: find the smallest digit larger than digits[i] to the right
        j = len(digits) - 1
        while digits[j] <= digits[i]:
            j -= 1
        
        # Step 3: swap
        digits[i], digits[j] = digits[j], digits[i]
        
        # Step 4: reverse the suffix
        digits[i + 1:] = reversed(digits[i + 1:])
        
        result = int("".join(digits))
        
        # Step 5: 32-bit integer check
        if result > 2**31 - 1:
            return -1
        
        return result
