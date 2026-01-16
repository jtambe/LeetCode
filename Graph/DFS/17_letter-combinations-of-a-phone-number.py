class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        def getKeyMap() -> dict:
            '''
            gets the keymap for numbers to letter mapping on the phone
            '''
            keymap = {}
            keymap['2'] = ['a','b','c']
            keymap['3'] = ['d','e','f']
            keymap['4'] = ['g','h','i']
            keymap['5'] = ['j','k','l']
            keymap['6'] = ['m','n','o']
            keymap['7'] = ['p','q','r','s']
            keymap['8'] = ['t','u','v']
            keymap['9'] = ['w','x','y','z']
            return keymap

        def recursive(curIndex:int, currentString:str, coveredLetters:set, digits:str, keymap:dict, solution: set):
            '''
            This recursive function will call itself until all the numbers in digits string are not traversed
            '''
            if(curIndex >= len(digits)):
                solution.add(currentString)
                currentString = ''
                return

            if curIndex < len(digits):
                for ch in keymap[digits[curIndex]]:
                    recursive(curIndex+1, currentString+ch, coveredLetters, digits, keymap, solution)
                        

        solution: set = set()
        keymap = getKeyMap()
        solution = set() # This is the solution set which will be returned at the end

        # for each letter in the starting number, run recursive DFS
        for ch in keymap[digits[0]]:
            recursive(0, '', set(), digits, keymap, solution)
        return list(solution);
