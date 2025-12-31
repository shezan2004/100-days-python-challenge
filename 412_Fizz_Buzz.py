class Solution(object):
    def fizzBuzz(self, n):
        answer = []
        
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        
        return answer
s = Solution()

# Test case 1: smallest valid input
print(s.fizzBuzz(1))
# Expected: ["1"]

# Test case 2: example input
print(s.fizzBuzz(3))
# Expected: ["1", "2", "Fizz"]

# Test case 3: multiple of 5
