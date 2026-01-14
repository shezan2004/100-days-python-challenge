class Solution(object):
    def solveEquation(self, equation):
        def evaluate(side):
            # Ensure signs are consistent for splitting
            # Replacing '-' with '+-' allows us to split by '+'
            tokens = side.replace('-', '+-').split('+')
            x_coeff = 0
            constant = 0
            
            for token in tokens:
                if not token:
                    continue
                if 'x' in token:
                    # Handle 'x', '+x', '-x'
                    if token == 'x' or token == '+x':
                        x_coeff += 1
                    elif token == '-x':
                        x_coeff -= 1
                    else:
                        # Extract the numerical coefficient before 'x'
                        x_coeff += int(token.replace('x', ''))
                else:
                    constant += int(token)
            return x_coeff, constant

        lhs, rhs = equation.split('=')
        l_x, l_c = evaluate(lhs)
        r_x, r_c = evaluate(rhs)

        # Resulting equation: a*x = b
        a = l_x - r_x
        b = r_c - l_c

        if a == 0:
            if b == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        
        return "x=" + str(b // a)