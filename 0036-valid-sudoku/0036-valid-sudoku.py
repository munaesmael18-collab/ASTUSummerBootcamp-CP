class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=list(set() for i in range(9))
        cols=list(set() for i in range(9) )
        boxes=list(set()  for i in range(9))
        for i in range(9):
            for j in range(9):
                num=board[i][j]
                if num==".":
                    continue
                box = (i // 3) * 3 + (j // 3)

                if num in rows[i]:
                    return False
                if num in cols[j]:
                    return False
                if num in boxes[box]:
                    return False

                rows[i].add(num)
                cols[j].add(num)
                boxes[box].add(num)

        return True