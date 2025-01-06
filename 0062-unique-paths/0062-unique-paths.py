class Solution(object):
    def uniquePaths(self, m, n):
        def bfs(i, j):
            paths = 0
            q = collections.deque()
            q.append((i, j))

            while q:
                row, col = q.popleft()

                if row == m - 1 and col == n - 1:
                    paths += 1
                    
                

                if row < m:
                    q.append((row + 1, col))
                


                if col < n:
                    q.append((row, col + 1))
            

            return paths
        

        return bfs(0, 0)
        