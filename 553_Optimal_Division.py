class Solution(object):
    def optimalDivision(self, nums):
        if len(nums) == 1:
            return str(nums[0])
        
        if len(nums) == 2:
            return str(nums[0]) + "/" + str(nums[1])
        
        # For 3 or more numbers
        first = str(nums[0])
        rest = "/".join(str(n) for n in nums[1:])
        return first + "/(" + rest + ")"
# Test cases
solution = Solution()

print(solution.optimalDivision([5]))
# Expected: "5"

print(solution.optimalDivision([10, 2]))
# Expected: "10/2"

print(solution.optimalDivision([2, 3, 4]))
# Expected: "2/(3/4)"

print(solution.optimalDivision([1000, 100, 10, 2]))
# Expected: "1000/(100/10/2)"

print(solution.optimalDivision([8, 4, 2, 1]))
# Expected: "8/(4/2/1)"

print(solution.optimalDivision([6, 3, 2]))
# Expected: "6/(3/2)"
