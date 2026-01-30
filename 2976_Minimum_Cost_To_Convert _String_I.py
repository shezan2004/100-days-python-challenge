class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        INF = 10**18
        
        # distance matrix for 26 letters
        dist = [[INF] * 26 for _ in range(26)]
        
        # zero cost to stay the same
        for i in range(26):
            dist[i][i] = 0
        
        # direct transformations
        for i in range(len(original)):
            u = ord(original[i]) - ord('a')
            v = ord(changed[i]) - ord('a')
            dist[u][v] = min(dist[u][v], cost[i])
        
        # Floyd–Warshall
        for k in range(26):
            for i in range(26):
                if dist[i][k] == INF:
                    continue
                for j in range(26):
                    if dist[k][j] == INF:
                        continue
                    new_cost = dist[i][k] + dist[k][j]
                    if new_cost < dist[i][j]:
                        dist[i][j] = new_cost
        
        # compute total cost
        total = 0
        for i in range(len(source)):
            s = ord(source[i]) - ord('a')
            t = ord(target[i]) - ord('a')
            if dist[s][t] == INF:
                return -1
            total += dist[s][t]
        
        return total
