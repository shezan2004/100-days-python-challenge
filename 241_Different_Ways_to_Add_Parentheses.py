class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        memo = {}

        def helper(expr):
            if expr in memo:
                return memo[expr]

            results = []

            for i, ch in enumerate(expr):
                if ch in '+-*':
                    left = helper(expr[:i])
                    right = helper(expr[i+1:])

                    for l in left:
                        for r in right:
                            if ch == '+':
                                results.append(l + r)
                            elif ch == '-':
                                results.append(l - r)
                            else:  # '*'
                                results.append(l * r)

            if not results:
                results.append(int(expr))

            memo[expr] = results
            return results

        return helper(expression)
solution = Solution()

tests = [
    ("3", [3]),
    ("1+2+3", [6, 6]),
    ("2*3*4", [24, 24]),
    ("5-3+1", [1, 3]),
    ("10+5*2", [20, 30]),
    ("0*1+2", [0, 2]),
    ("2-1-1", [0, 2]),
    ("2*3-4*5", [-34, -14, -10, -10, 10]),
]

for expr, expected in tests:
    result = sorted(solution.diffWaysToCompute(expr))
    print("Expression:", expr)
    print("Output:   ", result)
    print("Expected: ", sorted(expected))
    print("Pass:", result == sorted(expected))
    print("-" * 30)
