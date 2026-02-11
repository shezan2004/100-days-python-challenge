import sys
from collections import deque
from typing import List  # Required for older Python environments

# Increase recursion depth for deep segment tree queries
sys.setrecursionlimit(200000)

class SegmentTree:
    def __init__(self, data: List[int]):
        self.n = len(data)
        self.tree_min = [0] * (4 * self.n + 1)
        self.tree_max = [0] * (4 * self.n + 1)
        self.lazy = [0] * (4 * self.n + 1)
        if self.n > 0:
            self._build(data, 1, 1, self.n)

    def _pushup(self, i: int):
        self.tree_min[i] = min(self.tree_min[i << 1], self.tree_min[i << 1 | 1])
        self.tree_max[i] = max(self.tree_max[i << 1], self.tree_max[i << 1 | 1])

    def _apply(self, i: int, val: int):
        self.tree_min[i] += val
        self.tree_max[i] += val
        self.lazy[i] += val

    def _pushdown(self, i: int):
        if self.lazy[i] != 0:
            self._apply(i << 1, self.lazy[i])
            self._apply(i << 1 | 1, self.lazy[i])
            self.lazy[i] = 0

    def _build(self, data: List[int], i: int, l: int, r: int):
        if l == r:
            self.tree_min[i] = self.tree_max[i] = data[l - 1]
            return
        mid = (l + r) // 2
        self._build(data, i << 1, l, mid)
        self._build(data, i << 1 | 1, mid + 1, r)
        self._pushup(i)

    def update(self, i: int, l: int, r: int, target_l: int, target_r: int, val: int):
        if target_l <= l and r <= target_r:
            self._apply(i, val)
            return
        self._pushdown(i)
        mid = (l + r) // 2
        if target_l <= mid:
            self.update(i << 1, l, mid, target_l, target_r, val)
        if target_r > mid:
            self.update(i << 1 | 1, mid + 1, r, target_l, target_r, val)
        self._pushup(i)

    def find_last(self, i: int, l: int, r: int, target_l: int, target_r: int, val: int) -> int:
        if self.tree_min[i] > val or self.tree_max[i] < val:
            return -1
        if l == r:
            return l
        self._pushdown(i)
        mid = (l + r) // 2
        res = -1
        if target_r > mid:
            res = self.find_last(i << 1 | 1, mid + 1, r, target_l, target_r, val)
        if res == -1 and target_l <= mid:
            res = self.find_last(i << 1, l, mid, target_l, target_r, val)
        return res

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        
        def get_sgn(x):
            return 1 if x % 2 == 0 else -1

        occurrences = {}
        prefix_sum = [0] * n
        
        # Track first occurrences for the base prefix sum
        seen_first = set()
        curr_sum = 0
        for i in range(n):
            val = nums[i]
            if val not in occurrences:
                occurrences[val] = deque()
            occurrences[val].append(i + 1)
            
            if val not in seen_first:
                curr_sum += get_sgn(val)
                seen_first.add(val)
            prefix_sum[i] = curr_sum

        seg = SegmentTree(prefix_sum)
        max_len = 0
        current_offset = 0
        
        for i in range(n):
            # Find the furthest j such that prefix_sum[j] - current_offset == 0
            # We search in range [i + 1 + max_len, n] to optimize
            search_start = i + 1 + max_len
            if search_start <= n:
                last_idx = seg.find_last(1, 1, n, search_start, n, current_offset)
                if last_idx != -1:
                    max_len = last_idx - i

            # Move left boundary: Remove nums[i]
            val = nums[i]
            s = get_sgn(val)
            occurrences[val].popleft()
            
            # Its contribution (+1/-1) only existed from its index until its next occurrence
            next_idx = occurrences[val][0] if occurrences[val] else n + 1
            
            # Correcting the prefix sums in range [i+1, next_idx-1]
            if i + 1 <= next_idx - 1:
                seg.update(1, 1, n, i + 1, next_idx - 1, -s)
            
            # The baseline for "zero" shifts because we've passed this element
            current_offset -= s
            
        return max_len