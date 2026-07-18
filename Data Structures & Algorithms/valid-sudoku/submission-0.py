class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for  _  in range(9)]
        cols = [set() for  _ in range(9)]
        squares = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                x = board[i][j]
                if x == '.':
                    continue
                if x in rows[i] or x in cols[j] or x in squares[i//3*3+j//3]:
                    print(f"Duplicate found at {i=} and {j=}")
                    return False
                rows[i].add(x)
                cols[j].add(x)
                squares[i//3*3+j//3].add(x)
        
        return True