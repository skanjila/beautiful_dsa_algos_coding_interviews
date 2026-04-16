from typing import List


def simplify_path(path: str) -> str:
    """
    Normalize a Unix-style path by resolving '.', '..', and empty segments.

    Time complexity: O(N) because each path segment is parsed once.
    Space complexity: O(N) in the worst case for the stack of kept segments.
    """
    stack: List[str] = []

    for segment in path.split("/"):
        if not segment or segment == ".":
            continue
        if segment == "..":
            if stack:
                stack.pop()
        else:
            stack.append(segment)

    return "/" + "/".join(stack)
