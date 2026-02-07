class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        deletions = 0
        b_count = 0
        
        for char in s:
            if char == 'b':
                b_count += 1
            else:
                # We found an 'a'. 
                # Our options:
                # 1. Delete this 'a' (deletions + 1)
                # 2. Keep this 'a' and delete all previous 'b's (b_count)
                deletions = min(deletions + 1, b_count)
                
        return deletions