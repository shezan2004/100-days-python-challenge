class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        
        return result
s = Solution()

# Test case 1: Example from problem
print(s.threeSum([-1,0,1,2,-1,-4]))  
# Expected: [[-1,-1,2], [-1,0,1]]

# Test case 2: No valid triplets
print(s.threeSum([0,1,1]))  
# Expected: []

# Test case 3: All zeros
print(s.threeSum([0,0,0]))  
# Expected: [[0,0,0]]

# Test case 4: Larger mixed dataset
print(s.threeSum([3,-2,1,0,-1,2,-1,-4]))  
# Expected (order may vary): [[-4,1,3],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]

# Test case 5: No numbers
print(s.threeSum([]))  
# Expected: []

# Test case 6: Only two numbers
print(s.threeSum([1, -1]))  
# Expected: []

# Test case 7: Many duplicates
print(s.threeSum([1,1,1,1,-2,-2,-2,0,0,0]))  
# Expected: [[-2,1,1], [0,0,0]]

# Test case 8: Already sorted
print(s.threeSum([-5,-4,-3,0,1,2,3,4]))  
# Expected: e.g. [[-5,1,4], [-5,2,3], [-4,0,4], [-4,1,3], [-3,0,3], [-3,1,2]]
