class Solution(object):
    def exist(self, board, word):
        #dfs approach

        rows = len(board)
        cols = len(board[0])


        def dfs(i, j, index):

            if index == len(word):
                return True
            
            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != word[index]:
                return False
            
            tmp = board[i][j]
            board[i][j] = "#"

            res = (dfs(i + 1,j ,index + 1) or
                   dfs(i - 1, j,index + 1) or
                   dfs(i, j + 1, index + 1) or
                   dfs(i, j - 1, index + 1)
            )

            board[i][j] = tmp

            return res



        for i in range(rows):
            for j in range(cols):
                if dfs(i, j , 0):
                    return True
        return False
        