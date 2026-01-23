import random

class Solution(object):

    def __init__(self, nums):
        self.pos = {}

        for i in range(len(nums)):
            if nums[i] not in self.pos:
                self.pos[nums[i]] = []
            self.pos[nums[i]].append(i)

    def pick(self, target):
        return random.choice(self.pos[target])
