class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        max_length = 0

        # Outer loop for the start of the substring
        for i in range(n):
            freq = [0] * 26
            distinct_count = 0

            # Inner loop for the end of the substring
            for j in range(i, n):
                char_idx = ord(s[j]) - ord('a')
                
                if freq[char_idx] == 0:
                    distinct_count += 1
                freq[char_idx] += 1

                # The frequency that all distinct characters must match
                target_freq = freq[char_idx]
                is_balanced = True
                
                # Check if all characters encountered so far have the same target_freq
                for k in range(26):
                    if freq[k] > 0:
                        if freq[k] != target_freq:
                            is_balanced = False
                            break
                
                if is_balanced:
                    max_length = max(max_length, j - i + 1)
        
        return max_length