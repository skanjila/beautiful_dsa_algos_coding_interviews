from typing import List


def generate_anagrams(input_str: str)->List[str]:
    """Given an input string generate all the possible anagrams
    @param input_str: input string
    @return: list of all possible anagrams"""
    anagrams = []

    if not input_str:
        return [""]

    sorted_input_str = sorted(input_str)  # sorting enables the duplicate-skip trick
    length_of_input_str = len(sorted_input_str)
    used = [False] * length_of_input_str
    path = []
    results=[]

    def backtrack():
        if len(path) == length_of_input_str:
            results.append("".join(path))

        for i in range(length_of_input_str):
            if used[i]:
                continue
            if i > 0 and sorted_input_str[i] == sorted_input_str[i - 1] and not used[i - 1]:
                continue
            used[i] = True
            path.append(sorted_input_str[i])
            backtrack()
            path.pop()
            used[i] = False

    backtrack()
    return results
