class Solution(object):
    def isPowerOfThree(self, n):
        if n <= 0:
            return False
        
        while n % 3 == 0:
            n //= 3
        
        return n == 1
def test_isPowerOfThree():
    s = Solution()
    
    # true cases
    assert s.isPowerOfThree(1) == True     # 3^0
    assert s.isPowerOfThree(3) == True     # 3^1
    assert s.isPowerOfThree(9) == True     # 3^2
    assert s.isPowerOfThree(27) == True    # 3^3
    assert s.isPowerOfThree(1162261467) == True  # 3^19
    
    # false cases
    assert s.isPowerOfThree(0) == False
    assert s.isPowerOfThree(-1) == False
    assert s.isPowerOfThree(2) == False
    assert s.isPowerOfThree(6) == False
    assert s.isPowerOfThree(45) == False
    assert s.isPowerOfThree(2147483647) == False  # max 32-bit int
    
    print("All test cases passed!")
