from typing import List

def letter_combinations(digits: str) -> List[str]:
    """
    Given a string containing digits from 2-9 inclusive, return all possible
    letter combinations that the number could represent. Return the answer in any order.

    Approach: DFS + backtracking
    Time:  O(3^n) to O(4^n) depending on digits (n = len(digits))
    Space: O(n) recursion stack + O(result_size)
    """
    if not digits:
        return []

    keypad = {
        "2": "abc", "3": "def",
        "4": "ghi", "5": "jkl", "6": "mno",
        "7": "pqrs", "8": "tuv", "9": "wxyz",
    }

    result: List[str] = []
    path: List[str] = []

    def dfs(idx: int) -> None:
        # If we've assigned a letter for each digit, record the combination
        if idx == len(digits):
            result.append("".join(path))
            return

        for ch in keypad[digits[idx]]:
            path.append(ch)       # choose
            dfs(idx + 1)          # explore
            path.pop()            # un-choose (backtrack)

    dfs(0)
    return result
