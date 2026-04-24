class WordDictionary:
    def __init__(self):
        self.nodes = {}

    def addWord(self, word: str) -> None:
        word += '#'

        prev = self.nodes
        curr = prev.get(word[0])
        i = 0
        while curr is not None and i < len(word):
            i += 1
            prev = curr
            curr = curr.get(word[i])

        for j in range(i, len(word)):
            prev[word[j]] = {}
            prev = prev[word[j]]

    def search(self, word: str) -> bool:
        def recursiveSearch(w: str, node: dict) -> bool:
            if not w:
                return True

            if w[0] != ".":
                curr = node.get(w[0])
                if curr is None:
                    return False
                return recursiveSearch(w[1:], curr)

            for n in node.values():
                if recursiveSearch(w[1:], n):
                    return True
            return False

        return recursiveSearch(word + '#', self.nodes)


if __name__ == "__main__":
    wordDictionary = WordDictionary()
    wordDictionary.addWord("day")
    wordDictionary.addWord("bay")
    wordDictionary.addWord("may")
    assert not wordDictionary.search("say")
    assert wordDictionary.search("day")
    assert wordDictionary.search(".ay")
    assert wordDictionary.search("b..")
    wordDictionary.addWord("dog")
    assert not wordDictionary.search("do..")
    wordDictionary = WordDictionary()
    wordDictionary.addWord("complex")
    wordDictionary.addWord("complication")
    assert wordDictionary.search("c.mpl.x")
    assert wordDictionary.search("complic.tion")
    assert not wordDictionary.search("...........")
    assert not wordDictionary.search("c.....")
