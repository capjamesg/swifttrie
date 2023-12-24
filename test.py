import pytest
import swifttrie

print("Imported swifttrie")


@pytest.fixture(scope="session", autouse=True)
def insert_test():
    words = {"the": 0, "quick": 0}
    trie = swifttrie.SwiftTrie(words)
    return trie


def test_trie_structure(insert_test):
    trie = insert_test
    expected_structure = {"t": {"h": {"e": 0}}, "q": {"u": {"i": {"c": {"k": 0}}}}}
    assert trie.trie == expected_structure


def test_trie_search(insert_test):
    trie = insert_test

    assert trie.search("the") == 0
    assert trie.search("quick") == 0
    assert trie.search("not_in_trie") == None


def test_trie_insert(insert_test):
    trie = insert_test

    trie.insert({"taylor": 1, "swift": 2})
    assert trie.search("taylor") == 1
    assert trie.search("swift") == 2
    assert trie.search("swif") == {"t": 2}


def test_trie_remove(insert_test):
    trie = insert_test

    trie.remove("the")
    assert trie.search("the") == None
    assert trie.search("taylor") == 1
    assert trie.search("t") == {"a": {"y": {"l": {"o": {"r": 1}}}}}


def test_trie_reset(insert_test):
    trie = insert_test

    trie.reset()
    assert trie.trie == {}
