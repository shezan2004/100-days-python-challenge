class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
     
        if num1 == "0" or num2 == "0":
            return "0"
        
        m = len(num1)
        n = len(num2)
        
    
        result = [0] * (m + n)
        
       
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                pos1 = i + j
                pos2 = i + j + 1
                
                total = mul + result[pos2]
                result[pos2] = total % 10
                result[pos1] += total // 10
        
        res = []
        for digit in result:
            if not (len(res) == 0 and digit == 0):
                res.append(str(digit))
        
        return "".join(res)
    # Basic cases
print(Solution().multiply("2", "3"))        # Expected: "6"
print(Solution().multiply("123", "456"))    # Expected: "56088"

# Zero cases
print(Solution().multiply("0", "0"))        # Expected: "0"
print(Solution().multiply("0", "12345"))    # Expected: "0"
print(Solution().multiply("98765", "0"))    # Expected: "0"

# Single digit with multi-digit
print(Solution().multiply("9", "99"))       # Expected: "891"
print(Solution().multiply("7", "1234"))     # Expected: "8638"

# Large numbers
print(Solution().multiply("999", "999"))    # Expected: "998001"
print(Solution().multiply("123456789", "987654321"))  
# Expected: "121932631112635269"

# Same numbers
print(Solution().multiply("111", "111"))    # Expected: "12321"

