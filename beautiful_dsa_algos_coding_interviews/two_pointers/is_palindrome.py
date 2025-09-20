
def is_palindrome(s: str) -> bool:
    """Given a string, return whether it is a palindrome using teo pointers
    @param s: input string
    @return: whether s is a palindrome."""
    # first clean the string to remove characters that are not alpha numeric
    cleaned_s = ''.join(char.lower() for char in s if s if char.isalnum())

    left, right = 0, len(cleaned_s) - 1

    while left < right:
        # check to make sure that the character is an alphanumeric character
        if cleaned_s[left] != cleaned_s[right]:
            return False
        left += 1
        right -= 1
    return True