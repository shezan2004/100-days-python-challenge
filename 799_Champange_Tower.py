class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        # Create a 2D array (101x101) to handle the maximum constraints
        # tower[r][c] stores the total amount of champagne that flows into glass c of row r
        tower = [[0.0] * 101 for _ in range(101)]
        
        # Pour everything into the top glass initially
        tower[0][0] = float(poured)
        
        for r in range(query_row + 1):
            for c in range(r + 1):
                # Calculate how much is overflowing from the current glass
                overflow = (tower[r][c] - 1.0) / 2.0
                
                if overflow > 0:
                    # Distribute to the two glasses directly below
                    tower[r + 1][c] += overflow
                    tower[r + 1][c + 1] += overflow
        
        # The result cannot exceed 1.0 (the capacity of the glass)
        return min(1.0, tower[query_row][query_glass])