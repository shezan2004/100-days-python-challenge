class Solution(object):
    def divide(self, dividend, divisor):
        MAX_INT = 2147483647
        MIN_INT = -2147483648

        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        negative = (dividend < 0) != (divisor < 0)

        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)
        
        quotient = 0

        for i in range(31, -1, -1):
            if (abs_divisor << i) <= abs_dividend:
                abs_dividend -= (abs_divisor << i)
                quotient |= (1 << i)

        if negative:
            final_quotient = -quotient
        else:
            final_quotient = quotient

        if final_quotient < MIN_INT:
             return MIN_INT
        if final_quotient > MAX_INT:
             return MAX_INT

        return final_quotient

# Test Cases
if __name__ == '__main__':
    solution = Solution()

    # Normal cases
    print(solution.divide(10, 3))       # Expected: 3
    print(solution.divide(7, -3))      # Expected: -2
    print(solution.divide(-21, 5))      # Expected: -4
    print(solution.divide(-1, 1))       # Expected: -1
    print(solution.divide(-1, -1))      # Expected: 1
    print(solution.divide(0, 5))        # Expected: 0
    print(solution.divide(1, 1))        # Expected: 1

    # Edge cases
    print(solution.divide(2147483647, 1))         
    print(solution.divide(-2147483648, 1))        
    print(solution.divide(2147483647, -1))        
    print(solution.divide(2147483647, 2))         
    
    # Overflow case
    print(solution.divide(-2147483648, -1))       