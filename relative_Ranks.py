class Solution(object):
    def findRelativeRanks(self, score):
        n = len(score)
        sorted_scores = sorted(score, reverse=True)
        
        rank_map = {}
        for i in range(n):
            if i == 0:
                rank_map[sorted_scores[i]] = "Gold Medal"
            elif i == 1:
                rank_map[sorted_scores[i]] = "Silver Medal"
            elif i == 2:
                rank_map[sorted_scores[i]] = "Bronze Medal"
            else:
                rank_map[sorted_scores[i]] = str(i + 1)
        
        answer = []
        for s in score:
            answer.append(rank_map[s])
        
        return answer


# Test cases
sol = Solution()
print(sol.findRelativeRanks([5, 4, 3, 2, 1]))
print(sol.findRelativeRanks([10, 3, 8, 9, 4]))
print(sol.findRelativeRanks([1]))
print(sol.findRelativeRanks([100, 50, 200, 150]))
