from beautiful_dsa_algos_coding_interviews.two_pointers.is_palindrome import is_palindrome

def test_empty_string():
    assert is_palindrome("") is True

def test_single_char():
    assert is_palindrome("a") is True

def test_simple_palindrome():
    assert is_palindrome("madam") is True

def test_not_palindrome():
    assert is_palindrome("hello") is False

def test_mixed_case_and_non_alnum():
    assert is_palindrome("A man, a plan, a canal: Panama") is True

def test_with_numbers():
    assert is_palindrome("12321") is True
    assert is_palindrome("12345") is False
