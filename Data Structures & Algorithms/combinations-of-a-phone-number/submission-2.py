class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combinations = []
        curr_comb = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(i):
            if len(curr_comb) == len(digits):
                combinations.append("".join(curr_comb))
                return
            for c in digitToChar[digits[i]]:
                curr_comb.append(c)
                dfs(i + 1)
                curr_comb.pop()

        if digits:
            dfs(0)
        return combinations