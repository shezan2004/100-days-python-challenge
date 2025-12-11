# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1
class Solution(object):
    def firstUniqChar(self, s):
        counts = {}

        for c in s:
            if c in counts:
                counts[c] += 1
            else:
                counts[c] = 1

        for i in range(len(s)):
            if counts[s[i]] == 1:
                return i

        return -1
