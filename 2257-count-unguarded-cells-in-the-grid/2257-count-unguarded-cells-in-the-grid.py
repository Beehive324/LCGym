class Solution(object):
    def countUnguarded(self, m, n, guards, walls):

        matrix = [[0] * n for _ in range(m)]

        for dx,dy in walls:
            matrix[dx][dy] = 1
        
        for dx, dy in guards:
            matrix[dx][dy] = 1
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for dx, dy in guards:
            for x, y in directions:
                new_x = dx + x
                new_y = dy + y

                while 0 <= new_x < m and 0 <= new_y < n:

                    if matrix[new_x][new_y] == 1:
                        break
                    
                    if matrix[new_x][new_y] == 0:
                        matrix[new_x][new_y] = 3
                    
                    new_x += x
                    new_y += y
            
        
        count = sum(1 for r in range(m) for c in range(n) if matrix[r][c] == 0)


        return count