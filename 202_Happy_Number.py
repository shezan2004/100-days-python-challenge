class Solution(object):
    def isHappy(self, n):
    
        seen = set()
        
        while n != 1:
            if n in seen:
                return False
            
            seen.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))
        
        return True


# Test cases
solution = Solution()

print(solution.isHappy(19))  # True
print(solution.isHappy(2))   # False
print(solution.isHappy(1))   # True
print(solution.isHappy(7))   # True
print(solution.isHappy(20))  # False
