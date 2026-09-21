from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # brute force 
        row_check = defaultdict(set)
        col_check = defaultdict(set)
        box_check = defaultdict(set)

        # row check 
        for row in range(len(board)):
            for col in range(len(board[row])):
                row_value = board[row][col]

                if row_value == ".":
                    continue
                
                # check row already in the tracking dict
                elif row_value in row_check[row]:
                    return False
                
                # else add those 
                else:
                    row_check[row].add(row_value)

         # col check 
        for col in range(9):
            for row in range(9):
                col_value = board[row][col]

                if col_value == ".":
                    continue
                
                # check row already in the tracking dict
                elif col_value in col_check[col]:
                    return False
                
                # else add those 
                else:
                    col_check[col].add(col_value)
        
        # box check 
        # need to update the row and col 
        for r in range(0,9,3):
            for c in range(0,9,3):
                # create 3x3 check loops
                for row in range(r,3+r):
                    for col in range(c,3+c):
                        box_value = board[row][col]

                        if box_value == ".":
                            continue

                        elif box_value in box_check[(r,c)]:
                            return False

                        else:
                            box_check[(r,c)].add(box_value)

        return True

        
        