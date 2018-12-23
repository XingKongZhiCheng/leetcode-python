class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def detect(i, j):
            if board[i][j] != 'S' or (i, j) in seen:
                return
            # board[i][j] == 'S' 且没访问过四周
            seen.add((i, j))
            # up
            if i - 1 >= 0 and board[i - 1][j] == 'O':
                board[i - 1][j] = 'S'
                detect(i - 1, j)
            # down
            if i + 1 < rows and board[i + 1][j] == 'O':
                board[i + 1][j] = 'S'
                detect(i + 1, j)

            # left
            if j - 1 >= 0 and board[i][j - 1] == 'O':
                board[i][j - 1] = 'S'
                detect(i, j - 1)

            # right
            if j + 1 < cols and board[i][j + 1] == 'O':
                board[i][j + 1] = 'S'
                detect(i, j + 1)

        if not any(board):  # any():全部为 False，则返回 False，如果有一个为 True，则返回 True。
            return
        else:
            rows = len(board)
            cols = len(board[0])
            seen = set()
            for i, line in enumerate(board):
                for j, e in enumerate(line):
                    if e == 'O' and ((i in [0, rows-1]) or (j in [0, cols - 1])):
                        # 可以把初始的边界放到一个队列中，这样可以节省时间
                        board[i][j] = 'S'  # 边界'O'置为S
                        detect(i, j)  # 与'S'相邻的'O'置为S

        for i, line in enumerate(board):
            for j, e in enumerate(line):
                if e == 'O':  # 与'S'不相邻的'O'置为'X'
                    board[i][j] = 'X'

        for i, line in enumerate(board):
            for j, e in enumerate(line):
                if e == 'S':
                    board[i][j] = 'O'  # 边界'S'置为'O'
        return board


if __name__ == '__main__':
    sol = Solution()
    arr = [["O","X","O","O","O","O","O","O","O"],["O","O","O","X","O","O","O","O","X"],
           ["O","X","O","X","O","O","O","O","X"],["O","O","O","O","X","O","O","O","O"],
           ["X","O","O","O","O","O","O","O","X"],["X","X","O","O","X","O","X","O","X"],
           ["O","O","O","X","O","O","O","O","O"],["O","O","O","X","O","O","O","O","O"],
           ["O","O","O","O","O","X","X","O","O"]]
    # arr = [["O","X","O","O","O","X"],["O","O","X","X","X","O"],["X","X","X","X","X","O"],["O","O","O","O","X","X"],["X","X","O","O","X","O"],["O","O","X","X","X","X"]]
    # arr = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    print("result:", sol.solve(arr))
    answer = [["O","X","O","O","O","O","O","O","O"],["O","O","O","X","O","O","O","O","X"],
              ["O","X","O","X","O","O","O","O","X"],["O","O","O","O","X","O","O","O","O"],
              ["X","O","O","O","O","O","O","O","X"],["X","X","O","O","X","O","X","O","X"],
              ["O","O","O","X","O","O","O","O","O"],["O","O","O","X","O","O","O","O","O"],
              ["O","O","O","O","O","X","X","O","O"]]
    #answer = [["O","X","O","O","O","X"],["O","O","X","X","X","O"],["X","X","X","X","X","O"],["O","O","O","O","X","X"],["X","X","O","O","X","O"],["O","O","X","X","X","X"]]
    print("answer:", answer)