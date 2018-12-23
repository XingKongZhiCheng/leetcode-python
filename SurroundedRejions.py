class Solution:

    def solve(self, board):
        """
        ************* Time Limit Exceeded *****************
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return
        close_stack = []
        open_stack = []
        temp = set()  # -1
        rows = len(board)
        cols = len(board[0])

        if rows == 0 or cols == 0:
            return

        def isclose(i, j):
            if (i, j) in open_stack:
                return 0
            elif (i, j) in close_stack:
                return 1
            elif (i in [0, rows-1]) or (j in [0, cols - 1]):
                open_stack.append((i, j))
                return 0
            else:
                # 防止循环递归
                if (i, j) in seen:
                    return -1
                else:
                    seen.append((i, j))
                # 设置默认值 1
                # 只有r='O',才会递归，而递归是有返回值的
                r1, r2, r3, r4 = 1, 1, 1, 1

                # up
                if i-1 >= 0 and board[i-1][j] == 'O':
                    r1 = isclose(i-1, j)
                    if r1 == 0:
                        open_stack.append((i, j))
                        return 0
                # down
                if i+1 < rows and board[i+1][j] == 'O':
                    r2 = isclose(i+1, j)
                    if r2 == 0:
                        open_stack.append((i, j))
                        return 0
                # left
                if j-1 >= 0 and board[i][j-1] == 'O':
                    r3 = isclose(i, j-1)
                    if r3 == 0:
                        open_stack.append((i, j))
                        return 0
                # right
                if j+1 < cols and board[i][j+1] == 'O':
                    r4 = isclose(i, j+1)
                    if r4 == 0:
                        open_stack.append((i, j))
                        return 0

                # 没有一个方向为0
                if -1 not in [r1, r2, r3, r4]:
                    close_stack.append((i, j))
                    return 1
                else:
                    # 等待下次探查
                    temp.add(seen.pop(seen.index((i, j))))
                    return -1

        # seen
        seen = []  # 防止循环遍历
        for i, line in enumerate(board):
            for j, e in enumerate(line):
                if e == 'O':
                    isclose(i, j)

        # return
        for i, j in close_stack:
            board[i][j] = 'X'
        for i, j in temp:
            if (i, j) not in open_stack:
                board[i][j] = 'X'
        print('open_stack & close_stack:\n', set(open_stack) & set(close_stack))
        print("open_stack:\n", open_stack)
        print("close_stack:\n", close_stack)
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