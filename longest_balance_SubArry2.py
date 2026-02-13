class Solution(object):
    def longestBalanced(self, s):
        def get_max_for_subset(chars):
            # chars is a set, e.g., {'a', 'b'}
            max_len = 0
            # map of (difference_tuple) -> first_index_seen
            # For 2 chars, diff is (c1-c2). For 3, it's (c1-c2, c1-c3)
            lookup = {None: -1} 
            
            # Running counts
            counts = {c: 0 for c in chars}
            last_invalid = -1 # Track the last time a char NOT in subset appeared
            
            char_list = sorted(list(chars))
            
            # Initial state
            curr_diffs = tuple([0] * (len(char_list) - 1))
            lookup = {curr_diffs: -1}
            
            c_counts = {c: 0 for c in chars}
            
            for i, char in enumerate(s):
                if char not in chars:
                    # Reset when we hit a character outside our subset
                    c_counts = {c: 0 for c in chars}
                    curr_diffs = tuple([0] * (len(char_list) - 1))
                    lookup = {curr_diffs: i}
                    continue
                
                c_counts[char] += 1
                
                # Calculate differences relative to the first character in the subset
                # If counts are equal, all differences will be 0.
                diffs = []
                for j in range(1, len(char_list)):
                    diffs.append(c_counts[char_list[0]] - c_counts[char_list[j]])
                
                curr_diffs = tuple(diffs)
                
                if curr_diffs in lookup:
                    max_len = max(max_len, i - lookup[curr_diffs])
                else:
                    lookup[curr_diffs] = i
            return max_len

        # All non-empty subsets of {'a', 'b', 'c'}
        subsets = [
            {'a'}, {'b'}, {'c'},
            {'a', 'b'}, {'a', 'c'}, {'b', 'c'},
            {'a', 'b', 'c'}
        ]
        
        res = 0
        for sub in subsets:
            res = max(res, get_max_for_subset(sub))
        return res