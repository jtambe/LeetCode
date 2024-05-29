from typing import List
# https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
                
        i = 0
        dp = set()
        exists = False
        for x in range(rows):
            for y in range(cols):
                dp = set()
                exists = self.dfs(board, x, y, word, i, rows, cols, dp)
                if(exists):
                    return exists

        return False


    def dfs(self, board:List[List[str]], x:int, y:int, word:str, i: int, rows: int, cols: int, dp:set) -> bool:
        if(i == len(word)):
            return True
        if(x < 0 or y < 0 or x > rows-1 or y > cols -1 or word[i] != board[x][y] or ((x,y)) in dp):
            return False
       
        if(word[i] == board[x][y]):
            dp.add((x,y))
            print(f"board[{x}][{y}]:{board[x][y]}")
            print(dp)
            explore = \
            self.dfs(board, x+1, y, word, i+1, rows, cols, dp) or \
            self.dfs(board, x-1, y, word, i+1, rows, cols, dp) or \
            self.dfs(board, x, y+1, word, i+1, rows, cols, dp) or \
            self.dfs(board, x, y-1, word, i+1, rows, cols, dp)
            dp.remove((x,y))
            print(dp)
            return explore


        