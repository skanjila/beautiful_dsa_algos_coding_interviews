from beautiful_dsa_algos_coding_interviews.trie.implement_trie import Trie


def test_trie_operations():
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.search("app") is False
    assert trie.starts_with("app") is True
    trie.insert("app")
    assert trie.search("app") is True
