from typing import Dict, Any


class SwiftTrie:
    """
    A trie data structure implemented in Python.

    ref: https://en.wikipedia.org/wiki/Trie
    """

    def __init__(self, words: Dict[str, Any] = None):
        """
        Create a new trie.

        Args:
            words (Dict[str, Any], optional): A dictionary of words and their values. Defaults to None.

        Examples:
            >>> trie = SwiftTrie({"taylor": 1, "swift": 2})
            >>> trie.search("taylor")
            1
            >>> trie.search("swif")
            {"t": 2}
        """
        self.trie = {}

        if words is not None:
            self.insert(words)

    def traverse(self, trie: Dict[str, Any], word: str, idx: int = 0):
        """
        Traverse the trie to find the value associated with a word.

        The value can be a nested dictionary or a leaf node.

        Leaf nodes can be any type of object.

        Args:
            trie (Dict[str, Any]): The trie to traverse.
            word (str): The word to search for.
            idx (int): The current index of the word.

        Returns:
            Any: The value of the word or None if the word is not found.
        """
        letter = word[idx]

        if letter not in trie:
            return None

        if idx == len(word) - 1:
            return trie[letter]

        return self.traverse(trie[letter], word, idx + 1)

    def search(self, word: str):
        """
        Search for a word in the trie.

        Args:
            word (str): The word to search for.

        Returns:
            Any: The value of the word or None if the word is not found.

        Examples:
            >>> trie = SwiftTrie({"taylor": 1, "swift": 2})
            >>> trie.search("taylor")
            1
            >>> trie.search("swift")
            2
            >>> trie.search("swif")
            {"t": 2}
            None
        """
        return self.traverse(self.trie, word)

    def insert(self, words: Dict[str, Any]):
        """
        Insert an item into the trie.

        Args:
            words (Dict[str, Any]): A dictionary of words and their values.

        Examples:
            >>> trie = SwiftTrie()
            >>> trie.insert({"taylor": 1, "swift": 2})
        """
        trie = self.trie

        for word in words.keys():
            for i, letter in enumerate(word):
                if letter not in trie:
                    trie[letter] = {}

                if i == len(word) - 1:
                    trie[letter] = words[word]

                trie = trie[letter]

            trie = self.trie

    def remove(self, word: str):
        """
        Remove an item from the trie.

        Args:
            word (str): The word to remove.

        Examples:
            >>> trie = SwiftTrie({"taylor": 1, "swift": 2})
            >>> trie.remove("taylor")
            >>> trie.search("taylor")
            None
        """
        trie = self.trie

        if trie is None:
            return

        for i, letter in enumerate(word):
            if letter not in trie:
                return

            if i == len(word) - 1:
                del trie[letter]
                break

            trie = trie[letter]

        trie = self.trie

        self.clean(trie)

    def clean(self, trie: Dict[str, Any]):
        """
        Remove nodes without a value from the trie.

        Args:
            trie (Dict[str, Any]): The trie to clean.

        Returns:
            Dict[str, Any]: The cleaned trie.
        """
        for key in list(trie.keys()):
            if not isinstance(trie[key], dict):
                return None
            if trie[key] == {}:
                del trie[key]
            else:
                self.clean(trie[key])

    def reset(self):
        """
        Reset the trie.
        """
        self.trie = {}

    def __str__(self):
        return str(self.trie)
