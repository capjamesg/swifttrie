# swifttrie

An implementation of the [trie data structure](https://en.wikipedia.org/wiki/Trie).

The trie data structure is useful for building auto-complete text systems.

## Installation

You can only install `swifttrie` from source.

To do so, run the following commmands:

```
git clone https://github.com/capjamesg/swifttrie
cd swifttrie
pip3 install -e .
```

## Quickstart

With `swifttrie`, you can:

- Create a trie
- Add a word to a trie
- Retrieve a value from a trie
- Remove a word from a trie

### Create a trie

```python
from swifttrie import SwiftTrie

>>> trie = SwiftTrie({"taylor": 1, "swift": 2})
```

### Add a word to a trie

```python
from swifttrie import SwiftTrie

>>> trie.insert("taylor", 1)
```

### Retrieve a value from a trie

```python
>>> trie = SwiftTrie({"taylor": 1, "swift": 2})

>>> trie.search("taylor")
1
>>> trie.search("swif")
{"t": 2}
```

### Retrieve a word from a trie

```python
>>> trie = SwiftTrie({"taylor": 1, "swift": 2})

>>> trie.remove("taylor")

>>> trie.search("taylor")
None
```

## License

This project is licensed under an [MIT license](LICENSE).
