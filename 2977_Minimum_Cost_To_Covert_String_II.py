class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        n = len(source)
        INF = 10**18

        # Group rules by substring length
        by_len = {}
        for o, c, w in zip(original, changed, cost):
            L = len(o)
            if L not in by_len:
                by_len[L] = []
            by_len[L].append((o, c, w))

        # Collect all strings used in rules
        all_strings = set()
        for L in by_len:
            for o, c, _ in by_len[L]:
                all_strings.add(o)
                all_strings.add(c)

        # Map strings to indices
        idx = {s: i for i, s in enumerate(all_strings)}
        m = len(idx)

        # Build distance matrix
        dist = [[INF] * m for _ in range(m)]
        for i in range(m):
            dist[i][i] = 0

        for L in by_len:
            for o, c, w in by_len[L]:
                u = idx[o]
                v = idx[c]
                if w < dist[u][v]:
                    dist[u][v] = w

        # Floyd–Warshall
        for k in range(m):
            for i in range(m):
                if dist[i][k] == INF:
                    continue
                for j in range(m):
                    if dist[k][j] == INF:
                        continue
                    nd = dist[i][k] + dist[k][j]
                    if nd < dist[i][j]:
                        dist[i][j] = nd

        # DP
        dp = [INF] * (n + 1)
        dp[n] = 0

        lengths = list(by_len.keys())

        for i in range(n - 1, -1, -1):
            # Case: single character already matches
            if source[i] == target[i]:
                dp[i] = dp[i + 1]

            for L in lengths:
                j = i + L
                if j > n:
                    continue

                s = source[i:j]
                t = target[i:j]

                if s in idx and t in idx:
                    c = dist[idx[s]][idx[t]]
                    if c != INF and dp[j] != INF:
                        dp[i] = min(dp[i], c + dp[j])

        return -1 if dp[0] == INF else dp[0]
